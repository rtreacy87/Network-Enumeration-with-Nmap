"""High-level task implementations for each lab script."""

from __future__ import annotations

import argparse
import html
import os
import re
import socket
import time
import urllib.error
import xml.etree.ElementTree as ET
from typing import List, Optional, Sequence, Tuple

from .dns import query_dns_version_bind
from .nmap import (
    parse_host_from_service_info,
    parse_netbios_name,
    parse_open_ports_from_greppable,
    parse_open_ports_from_nmap_table,
    parse_open_services_from_xml,
    run_banner_scripts,
    run_nbstat,
    run_nse_discovery,
    run_service_scan,
    scan_all_tcp_open_greppable,
    scan_all_tcp_open_xml,
    scan_full_tcp_with_source_port_53,
)
from .patterns import extract_flag
from .shell import run_command_allow_timeout, run_command_strict
from .web import fetch_url, get_alert_count


COMMON_HTTP_PATHS = [
    "/robots.txt",
    "/sitemap.xml",
    "/.well-known/security.txt",
]


def _extract_http_targets(discovery_output: str, target: str) -> List[str]:
    candidates = set()
    url_pattern = re.compile(r"https?://[^\s)>'\"]+")
    path_pattern = re.compile(r"\b/(?:[A-Za-z0-9._~!$&'()*+,;=:@%-]+/?)+")

    for match in url_pattern.findall(discovery_output):
        candidates.add(match.rstrip(".,;"))

    for match in path_pattern.findall(discovery_output):
        if not match.startswith("//"):
            candidates.add(f"http://{target}{match}")

    return sorted(candidates)


def _build_basic_html_report(html_path: str, target: str, ports: List[Tuple[int, str]]) -> None:
    rows = [f"<tr><td>{port}</td><td>{html.escape(service)}</td><td>open</td></tr>" for port, service in ports]
    table_rows = "\n".join(rows) if rows else "<tr><td colspan='3'>No open TCP ports found</td></tr>"

    doc = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Nmap Report - {html.escape(target)}</title>
  <style>
    body {{ font-family: sans-serif; margin: 2rem; background: #f7f7f7; color: #111; }}
    .card {{ background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 1rem 1.25rem; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; }}
    th, td {{ border: 1px solid #ddd; padding: 0.5rem; text-align: left; }}
    th {{ background: #f0f0f0; }}
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Nmap Report</h1>
    <p><strong>Target:</strong> {html.escape(target)}</p>
    <p><strong>Open TCP ports:</strong> {len(ports)}</p>
    <table>
      <thead>
        <tr><th>Port</th><th>Service</th><th>State</th></tr>
      </thead>
      <tbody>
        {table_rows}
      </tbody>
    </table>
  </div>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as handle:
        handle.write(doc)


def _parse_open_ports_from_xml_file(xml_path: str) -> List[Tuple[int, str]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    result: List[Tuple[int, str]] = []

    for port in root.findall(".//host/ports/port"):
        if port.get("protocol") != "tcp":
            continue
        state = port.find("state")
        if state is None or state.get("state") != "open":
            continue
        port_id = port.get("portid", "")
        if not port_id.isdigit():
            continue
        service_el = port.find("service")
        service = service_el.get("name", "unknown") if service_el is not None else "unknown"
        result.append((int(port_id), service))

    result.sort(key=lambda item: item[0])
    return result


def _create_html_report(xml_path: str, html_path: str, target: str, ports: List[Tuple[int, str]]) -> str:
    try:
        run_command_strict(["xsltproc", xml_path, "-o", html_path])
        return "xsltproc"
    except Exception:
        _build_basic_html_report(html_path, target, ports)
        return "python-fallback"


def scan_target_task(target: str) -> int:
    open_ports = parse_open_ports_from_greppable(scan_all_tcp_open_greppable(target))

    hostname = None
    if open_ports:
        service_output = run_service_scan(target, open_ports)
        hostname = parse_host_from_service_info(service_output)

    if not hostname:
        hostname = parse_netbios_name(run_nbstat(target))

    print(f"Target: {target}")
    print(f"Open TCP Ports ({len(open_ports)}): {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Total Open TCP Ports: {len(open_ports)}")
    print(f"Hostname: {hostname if hostname else 'Not found'}")
    return 0


def scan_and_report_task(target: str, basename: str) -> int:
    run_command_strict([
        "nmap",
        "-p-",
        "-Pn",
        "--open",
        "-T4",
        "--min-rate",
        "5000",
        "-oA",
        basename,
        target,
    ])

    xml_path = f"{basename}.xml"
    html_path = f"{basename}.html"
    if not os.path.exists(xml_path):
        raise FileNotFoundError(f"Expected XML output was not found: {xml_path}")

    open_ports = _parse_open_ports_from_xml_file(xml_path)
    method = _create_html_report(xml_path, html_path, target, open_ports)
    highest_port = max((port for port, _ in open_ports), default=None)

    print(f"Target: {target}")
    print(f"Output files: {basename}.nmap, {basename}.gnmap, {basename}.xml, {basename}.html")
    print(f"HTML generation: {method}")
    print(f"Open TCP ports: {', '.join(str(port) for port, _ in open_ports) if open_ports else 'None'}")
    print(f"Highest open TCP port: {highest_port if highest_port is not None else 'None'}")
    return 0


def service_flag_task(target: str) -> int:
    scan_xml = scan_all_tcp_open_xml(target)
    open_ports, services = parse_open_services_from_xml(scan_xml)
    banner_output = run_banner_scripts(target, open_ports)
    flag = extract_flag(f"{scan_xml}\n{banner_output}")

    print(f"Target: {target}")
    print(f"Open TCP ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print("Services:")
    for port in open_ports:
        print(f"  {port}/tcp -> {services.get(port, 'unknown')}")
    print("Banner scan output:")
    print(banner_output.strip() if banner_output.strip() else "<none>")
    print(f"Flag: {flag if flag else 'Not found'}")
    return 0


def nse_flag_task(target: str) -> int:
    open_ports = parse_open_ports_from_greppable(scan_all_tcp_open_greppable(target))
    discovery_ports = [port for port in open_ports if port in {80, 443, 8080, 8443}]

    try:
        discovery_output = run_nse_discovery(target, discovery_ports, timeout_seconds=60)
    except Exception:
        discovery_output = ""

    fetched_results: List[Tuple[str, str]] = []
    flag = extract_flag(discovery_output)

    if not flag and discovery_output:
        for url in _extract_http_targets(discovery_output, target):
            try:
                content, _ = fetch_url(url, timeout=15)
            except Exception:
                continue
            fetched_results.append((url, content))
            flag = extract_flag(content)
            if flag:
                break

    if not flag and discovery_ports:
        for path in COMMON_HTTP_PATHS:
            url = f"http://{target}{path}"
            if any(existing == url for existing, _ in fetched_results):
                continue
            try:
                content, _ = fetch_url(url, timeout=15)
            except Exception:
                continue
            fetched_results.append((url, content))
            flag = extract_flag(content)
            if flag:
                break

    if not flag:
        flag = extract_flag(discovery_output)

    print(f"Target: {target}")
    print(f"Open TCP ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print("Discovery output:")
    print(discovery_output.strip() if discovery_output.strip() else "<none>")
    if fetched_results:
        print("Fetched discovery URLs:")
        for url, content in fetched_results:
            first_line = content.strip().splitlines()[0] if content.strip() else "<empty>"
            print(f"  {url} -> {first_line}")
    print(f"Flag: {flag if flag else 'Not found'}")
    return 0 if flag else 1


def quiet_os_task(target: str) -> int:
    before_alerts = get_alert_count(target)

    ssh_banner = ""
    try:
        with socket.create_connection((target, 22), timeout=5) as sock:
            sock.settimeout(5)
            ssh_banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
    except OSError:
        pass

    http_server = ""
    try:
        _, headers = fetch_url(f"http://{target}/", method="HEAD", timeout=10)
        http_server = headers.get("Server", "")
    except (OSError, urllib.error.URLError):
        pass

    combined = f"{ssh_banner} {http_server}".lower()
    os_name = "Unknown"
    for needle, label in [
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
    ]:
        if needle in combined:
            os_name = label
            break

    if os_name == "Unknown" and ("linux" in combined or ssh_banner or http_server):
        os_name = "Linux"

    after_alerts = get_alert_count(target)

    print(f"Target: {target}")
    print(f"Alerts before: {before_alerts if before_alerts is not None else 'Unknown'}")
    print(f"SSH banner: {ssh_banner if ssh_banner else 'Unavailable'}")
    print(f"HTTP server: {http_server if http_server else 'Unavailable'}")
    print(f"Alerts after: {after_alerts if after_alerts is not None else 'Unknown'}")
    if before_alerts is not None and after_alerts is not None:
        print(f"Alert delta: {after_alerts - before_alerts}")
    print(f"OS: {os_name}")
    return 0 if os_name != "Unknown" else 1


def quiet_dns_version_task(target: str) -> int:
    before = get_alert_count(target)
    version = query_dns_version_bind(target)
    after = get_alert_count(target)

    print(f"Target: {target}")
    print(f"Alerts before: {before if before is not None else 'Unknown'}")
    print(f"DNS version: {version if version else 'Not found'}")
    print(f"Alerts after: {after if after is not None else 'Unknown'}")
    if before is not None and after is not None:
        print(f"Alert delta: {after - before}")
    return 0 if version else 1


def _detect_source_ip_for_target(target: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((target, 53))
        return sock.getsockname()[0]


def _grab_flag_from_50000(target: str, source_ip: str, timeout: int) -> str:
    attempts = [
        ["nc", "-nv", "-w", str(timeout), "-s", source_ip, "-p", "53", target, "50000"],
        ["nc", "-nv", "-s", source_ip, "-p", "53", target, "50000"],
    ]
    outputs: List[str] = []

    for index, cmd in enumerate(attempts, start=1):
        result = run_command_allow_timeout(cmd, timeout=timeout, stdin_data="\r\n")
        text = f"{result.stdout}\n{result.stderr}".strip()
        label = f"[nc attempt {index}{' timed out' if result.timed_out else ''}]"
        outputs.append(f"{label}\n{text}".strip())
        if extract_flag(text):
            break
        time.sleep(1)

    return "\n\n".join(outputs).strip()


def hard_lab_service_version_task(target: str, source_ip: Optional[str], nc_timeout: int) -> int:
    if os.geteuid() != 0:
        print(
            "Error: this script must be run as root (use sudo) to perform -g53 scans.",
            file=sys.stderr,
        )
        return 2

    before = get_alert_count(target)
    scan_output = scan_full_tcp_with_source_port_53(target)
    after = get_alert_count(target)

    open_ports = parse_open_ports_from_nmap_table(scan_output)
    chosen_source_ip = source_ip or "Not used"
    nc_output = ""

    if 50000 in open_ports:
        chosen_source_ip = source_ip or _detect_source_ip_for_target(target)
        nc_output = _grab_flag_from_50000(target, chosen_source_ip, nc_timeout)

    flag = extract_flag(f"{scan_output}\n{nc_output}")

    print(f"Target: {target}")
    print(f"Alerts before: {before if before is not None else 'Unknown'}")
    print("Raw scan output:")
    print(scan_output.strip())
    print(f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Source IP used: {chosen_source_ip}")
    print("nc output:")
    print(nc_output if nc_output else "<not executed>")
    print(f"Alerts after: {after if after is not None else 'Unknown'}")
    if before is not None and after is not None:
        print(f"Alert delta: {after - before}")
    print(f"Flag: {flag if flag else 'Not found'}")

    return 0 if flag else 1


# CLI wrappers used by top-level scripts.
def cli_scan_target(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Find open TCP ports and target hostname")
    parser.add_argument("target", help="Target IP or hostname")
    args = parser.parse_args(argv)
    return scan_target_task(args.target)


def cli_scan_and_report(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Full TCP scan with HTML report generation")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--basename", default="target", help="Output base filename (default: target)")
    args = parser.parse_args(argv)
    return scan_and_report_task(args.target, args.basename)


def cli_service_flag(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Enumerate services and find embedded flag")
    parser.add_argument("target", help="Target IP")
    args = parser.parse_args(argv)
    return service_flag_task(args.target)


def cli_nse_flag(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Find a service flag using Nmap NSE scripts")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args(argv)
    return nse_flag_task(args.target)


def cli_quiet_os(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Quietly identify the target operating system")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args(argv)
    return quiet_os_task(args.target)


def cli_quiet_dns(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Quietly identify a DNS server version over UDP")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args(argv)
    return quiet_dns_version_task(args.target)


def cli_hard_lab(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Solve hard IDS/IPS lab with source-port-53 scan")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("--source-ip", help="Your VPN/source IP for nc -s (PWNIP).")
    parser.add_argument(
        "--nc-timeout",
        type=int,
        default=25,
        help="Seconds to wait for nc response before collecting partial output (default: 25)",
    )
    args = parser.parse_args(argv)
    return hard_lab_service_version_task(args.target, args.source_ip, args.nc_timeout)
