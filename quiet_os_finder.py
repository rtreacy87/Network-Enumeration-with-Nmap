#!/usr/bin/env python3
"""Identify the target OS with minimal IDS/IPS alerts.

Usage:
  python3 quiet_os_finder.py 10.129.2.80
"""

import argparse
import re
import socket
import sys
import urllib.error
import urllib.request
from typing import Optional, Tuple


def fetch_url(url: str, method: str = "GET", timeout: int = 10) -> Tuple[str, dict]:
    request = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8", errors="ignore")
        headers = {key: value for key, value in response.headers.items()}
        return body, headers


def get_alert_count(target: str) -> Optional[int]:
    body, _ = fetch_url(f"http://{target}/status.php")
    match = re.search(r"Recorded alerts:\s*(\d+)\s*/\s*100\s*alerts", body, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def get_ssh_banner(target: str, timeout: int = 5) -> str:
    with socket.create_connection((target, 22), timeout=timeout) as sock:
        sock.settimeout(timeout)
        return sock.recv(1024).decode("utf-8", errors="ignore").strip()


def get_http_server_header(target: str, timeout: int = 10) -> str:
    _, headers = fetch_url(f"http://{target}/", method="HEAD", timeout=timeout)
    return headers.get("Server", "")


def infer_os(ssh_banner: str, http_server: str) -> str:
    combined = f"{ssh_banner} {http_server}".lower()

    indicators = [
        ("ubuntu", "Ubuntu"),
        ("debian", "Debian"),
        ("centos", "CentOS"),
        ("red hat", "Red Hat"),
        ("fedora", "Fedora"),
        ("freebsd", "FreeBSD"),
        ("windows", "Windows"),
        ("openbsd", "OpenBSD"),
        ("suse", "SUSE"),
        ("alpine", "Alpine Linux"),
    ]

    for needle, name in indicators:
        if needle in combined:
            return name

    if "linux" in combined or ssh_banner or http_server:
        return "Linux"

    return "Unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description="Quietly identify the target operating system")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args()

    before_alerts = get_alert_count(args.target)
    ssh_banner = ""
    http_server = ""

    try:
        ssh_banner = get_ssh_banner(args.target)
    except OSError:
        pass

    try:
        http_server = get_http_server_header(args.target)
    except (OSError, urllib.error.URLError):
        pass

    os_name = infer_os(ssh_banner, http_server)
    after_alerts = get_alert_count(args.target)

    print(f"Target: {args.target}")
    print(f"Alerts before: {before_alerts if before_alerts is not None else 'Unknown'}")
    print(f"SSH banner: {ssh_banner if ssh_banner else 'Unavailable'}")
    print(f"HTTP server: {http_server if http_server else 'Unavailable'}")
    print(f"Alerts after: {after_alerts if after_alerts is not None else 'Unknown'}")
    if before_alerts is not None and after_alerts is not None:
        print(f"Alert delta: {after_alerts - before_alerts}")
    print(f"OS: {os_name}")

    return 0 if os_name != "Unknown" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
