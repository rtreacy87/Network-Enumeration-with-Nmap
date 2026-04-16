"""Nmap-specific command wrappers and output parsing."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple

from .shell import run_command_strict


def scan_all_tcp_open_greppable(target: str, min_rate: int = 5000) -> str:
    return run_command_strict([
        "nmap",
        "-p-",
        "--min-rate",
        str(min_rate),
        "-T4",
        "--open",
        "-Pn",
        target,
        "-oG",
        "-",
    ])


def parse_open_ports_from_greppable(output: str) -> List[int]:
    for line in output.splitlines():
        if "Ports:" not in line:
            continue
        ports: List[int] = []
        for item in line.split("Ports:", 1)[1].split(","):
            item = item.strip()
            if "/open/tcp" not in item:
                continue
            port_str = item.split("/", 1)[0].strip()
            if port_str.isdigit():
                ports.append(int(port_str))
        return sorted(set(ports))
    return []


def scan_all_tcp_open_xml(target: str, min_rate: int = 5000) -> str:
    return run_command_strict([
        "nmap",
        "-p-",
        "--open",
        "-Pn",
        "-n",
        "-T4",
        "--min-rate",
        str(min_rate),
        "-oX",
        "-",
        target,
    ])


def parse_open_services_from_xml(xml_text: str) -> Tuple[List[int], Dict[int, str]]:
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
        if not portid.isdigit():
            continue
        number = int(portid)
        open_ports.append(number)
        service = port.find("service")
        services[number] = service.get("name", "unknown") if service is not None else "unknown"

    return sorted(set(open_ports)), services


def run_service_scan(target: str, ports: List[int]) -> str:
    if not ports:
        return ""
    return run_command_strict(["nmap", "-sV", "-Pn", "-p", ",".join(map(str, ports)), target])


def parse_host_from_service_info(service_scan_output: str) -> Optional[str]:
    match = re.search(r"Service Info:\s*Host:\s*([^;\s]+)", service_scan_output)
    return match.group(1).strip() if match else None


def run_nbstat(target: str) -> str:
    return run_command_strict(["nmap", "-p139,445", "--script", "nbstat", "-Pn", target])


def parse_netbios_name(text: str) -> Optional[str]:
    match = re.search(r"NetBIOS name:\s*([A-Za-z0-9._-]+)", text)
    return match.group(1).strip() if match else None


def run_banner_scripts(target: str, ports: List[int]) -> str:
    if not ports:
        return ""
    return run_command_strict([
        "nmap",
        "-sV",
        "--version-light",
        "-Pn",
        "-n",
        "-p",
        ",".join(map(str, ports)),
        "--script",
        "banner,ftp-syst,ftp-anon,http-title",
        target,
    ])


def run_nse_discovery(target: str, ports: List[int], timeout_seconds: int = 60) -> str:
    if not ports:
        return ""
    return run_command_strict([
        "nmap",
        "-Pn",
        "-n",
        "-p",
        ",".join(map(str, ports)),
        "--script",
        "discovery",
        target,
    ], timeout=timeout_seconds)


def scan_full_tcp_with_source_port_53(target: str) -> str:
    return run_command_strict([
        "nmap",
        "-g53",
        "--max-retries=1",
        "-Pn",
        "-p-",
        "--disable-arp-ping",
        target,
    ], timeout=180)


def parse_open_ports_from_nmap_table(output: str) -> List[int]:
    ports: List[int] = []
    for line in output.splitlines():
        match = re.match(r"^(\d+)/tcp\s+open\b", line.strip())
        if match:
            ports.append(int(match.group(1)))
    return sorted(set(ports))
