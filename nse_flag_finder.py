#!/usr/bin/env python3
"""Use Nmap NSE scripts to find a flag exposed by one of the target services.

Usage:
  python3 nse_flag_finder.py 10.129.1.51
"""

import argparse
import re
import subprocess
import sys
from typing import List, Optional


FLAG_PATTERNS = [
    r"HTB\{[^\r\n}]+\}",
    r"FLAG\{[^\r\n}]+\}",
    r"flag\{[^\r\n}]+\}",
]


COMMON_HTTP_PATHS = [
    "/robots.txt",
    "/sitemap.xml",
    "/.well-known/security.txt",
]


def run_cmd(cmd: List[str], timeout: Optional[int] = None) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def find_open_ports(target: str) -> List[int]:
    output = run_cmd([
        "nmap",
        "-p-",
        "--open",
        "-Pn",
        "-n",
        "--min-rate",
        "5000",
        "-T4",
        "-oG",
        "-",
        target,
    ], timeout=40)

    for line in output.splitlines():
        if "Ports:" not in line:
            continue
        ports = []
        for item in line.split("Ports:", 1)[1].split(","):
            item = item.strip()
            if "/open/tcp" not in item:
                continue
            port_str = item.split("/", 1)[0].strip()
            if port_str.isdigit():
                ports.append(int(port_str))
        return sorted(ports)

    return []


def run_discovery_nse(target: str, ports: List[int]) -> str:
    if not ports:
        return ""

    return run_cmd([
        "nmap",
        "-Pn",
        "-n",
        "-p",
        ",".join(str(port) for port in ports),
        "--script",
        "discovery",
        target,
    ], timeout=60)


def extract_http_targets(discovery_output: str, target: str) -> List[str]:
    candidates = set()

    url_pattern = re.compile(r"https?://[^\s)>'\"]+")
    path_pattern = re.compile(r"\b/(?:[A-Za-z0-9._~!$&'()*+,;=:@%-]+/?)+")

    for match in url_pattern.findall(discovery_output):
        candidates.add(match.rstrip('.,;'))

    for match in path_pattern.findall(discovery_output):
        if match.startswith("//"):
            continue
        candidates.add(f"http://{target}{match}")

    return sorted(candidates)


def fetch_url(url: str) -> str:
    return run_cmd(["curl", "-fsSL", url], timeout=15)


def extract_flag(text: str) -> str | None:
    for pattern in FLAG_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Find a service flag using Nmap NSE scripts")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args()

    open_ports = find_open_ports(args.target)
    discovery_ports = [port for port in open_ports if port in {80, 443, 8080, 8443}]
    try:
        discovery_output = run_discovery_nse(args.target, discovery_ports)
    except Exception:
        discovery_output = ""
    fetched_results: List[tuple[str, str]] = []
    flag = extract_flag(discovery_output)

    if not flag and discovery_output:
        for url in extract_http_targets(discovery_output, args.target):
            try:
                content = fetch_url(url)
            except Exception:
                continue
            fetched_results.append((url, content))
            flag = extract_flag(content)
            if flag:
                break

    if not flag and discovery_ports:
        for path in COMMON_HTTP_PATHS:
            url = f"http://{args.target}{path}"
            if any(existing_url == url for existing_url, _ in fetched_results):
                continue
            try:
                content = fetch_url(url)
            except Exception:
                continue
            fetched_results.append((url, content))
            flag = extract_flag(content)
            if flag:
                break

    if not flag:
        flag = extract_flag(discovery_output)

    print(f"Target: {args.target}")
    print(f"Open TCP ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print("Discovery output:")
    print(discovery_output.strip() if discovery_output.strip() else "<none>")
    if fetched_results:
        print("Fetched discovery URLs:")
        for url, content in fetched_results:
            preview = content.strip().splitlines()[0] if content.strip() else "<empty>"
            print(f"  {url} -> {preview}")
    print(f"Flag: {flag if flag else 'Not found'}")

    return 0 if flag else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
