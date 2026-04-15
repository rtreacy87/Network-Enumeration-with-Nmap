#!/usr/bin/env python3
"""Enumerate all TCP ports/services and extract a flag from service output.

Usage:
  python3 service_flag_finder.py 10.129.2.49
"""

import argparse
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple


FLAG_PATTERNS = [
    r"HTB\{[^\n\r}]+\}",
    r"flag\{[^\n\r}]+\}",
    r"FLAG\{[^\n\r}]+\}",
]


def run_cmd(cmd: List[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def scan_open_ports_and_services(target: str) -> Tuple[List[int], Dict[int, str], str]:
    xml_text = run_cmd([
        "nmap",
        "-p-",
        "--open",
        "-Pn",
        "-n",
        "-T4",
        "--min-rate",
        "5000",
        "-oX",
        "-",
        target,
    ])

    root = ET.fromstring(xml_text)
    open_ports: List[int] = []
    services: Dict[int, str] = {}
    for port in root.findall(".//host/ports/port"):
        if port.get("protocol") != "tcp":
            continue
        state = port.find("state")
        if state is None or state.get("state") != "open":
            continue
        portid = port.get("portid", "")
        if portid.isdigit():
            p = int(portid)
            open_ports.append(p)
            service = port.find("service")
            name = service.get("name", "unknown") if service is not None else "unknown"
            services[p] = name

    return sorted(set(open_ports)), services, xml_text


def scan_banners(target: str, ports: List[int]) -> str:
    if not ports:
        return ""
    ports_csv = ",".join(str(p) for p in ports)
    return run_cmd([
        "nmap",
        "-sV",
        "--version-light",
        "-Pn",
        "-n",
        "-p",
        ports_csv,
        "--script",
        "banner,ftp-syst,ftp-anon,http-title",
        target,
    ])


def find_flag(text: str) -> Optional[str]:
    for pattern in FLAG_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Enumerate services and find embedded flag")
    parser.add_argument("target", help="Target IP")
    args = parser.parse_args()

    target = args.target

    open_ports, services, scan_xml = scan_open_ports_and_services(target)

    banner_output = scan_banners(target, open_ports)
    combined_text_parts = [scan_xml, banner_output]

    combined_text = "\n".join(combined_text_parts)
    flag = find_flag(combined_text)

    print(f"Target: {target}")
    print(f"Open TCP ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print("Services:")
    for port in open_ports:
        print(f"  {port}/tcp -> {services.get(port, 'unknown')}")

    print("Banner scan output:")
    print(banner_output.strip() if banner_output.strip() else "<none>")

    print(f"Flag: {flag if flag else 'Not found'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
