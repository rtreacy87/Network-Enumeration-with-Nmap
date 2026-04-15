#!/usr/bin/env python3
"""Find all open TCP ports and enumerate hostname for a target using nmap.

Usage:
  python3 scan_target.py 10.129.2.49
"""

import argparse
import re
import subprocess
import sys
from typing import List, Optional


def run_cmd(cmd: List[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def find_open_ports(target: str) -> List[int]:
    # High min-rate keeps the full 1-65535 scan quick on HTB-style labs.
    output = run_cmd([
        "nmap",
        "-p-",
        "--min-rate",
        "5000",
        "-T4",
        "--open",
        "-Pn",
        target,
        "-oG",
        "-",
    ])

    for line in output.splitlines():
        if "Ports:" not in line:
            continue
        ports_part = line.split("Ports:", 1)[1]
        ports: List[int] = []
        for item in ports_part.split(","):
            item = item.strip()
            if "/open/tcp" in item:
                port_str = item.split("/", 1)[0].strip()
                if port_str.isdigit():
                    ports.append(int(port_str))
        return sorted(ports)

    return []


def find_hostname(target: str, open_ports: List[int]) -> Optional[str]:
    if not open_ports:
        return None

    ports_csv = ",".join(str(p) for p in open_ports)
    output = run_cmd(["nmap", "-sV", "-Pn", "-p", ports_csv, target])

    # Example: Service Info: Host: NIX-NMAP-DEFAULT; OS: Linux; ...
    match = re.search(r"Service Info:\s*Host:\s*([^;\s]+)", output)
    if match:
        return match.group(1).strip()

    # Fallback to nbstat if service info does not include host.
    nb_output = run_cmd(["nmap", "-p139,445", "--script", "nbstat", "-Pn", target])
    match = re.search(r"NetBIOS name:\s*([A-Za-z0-9._-]+)", nb_output)
    if match:
        return match.group(1).strip()

    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Find open TCP ports and target hostname")
    parser.add_argument("target", help="Target IP or hostname")
    args = parser.parse_args()

    target = args.target
    open_ports = find_open_ports(target)
    hostname = find_hostname(target, open_ports)

    print(f"Target: {target}")
    print(f"Open TCP Ports ({len(open_ports)}): {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Total Open TCP Ports: {len(open_ports)}")
    print(f"Hostname: {hostname if hostname else 'Not found'}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
