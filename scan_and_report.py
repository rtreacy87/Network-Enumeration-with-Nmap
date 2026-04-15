#!/usr/bin/env python3
"""Run a full TCP scan, save nmap outputs, and generate an HTML report.

Usage:
  python3 scan_and_report.py 10.129.1.50
"""

import argparse
import html
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from typing import List, Tuple


def run_cmd(cmd: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def run_full_scan(target: str, base_name: str) -> None:
    cmd = ["nmap", "-p-", "-Pn", "--open", "-T4", "--min-rate", "5000", "-oA", base_name, target]
    proc = run_cmd(cmd)
    if proc.returncode != 0:
        raise RuntimeError(f"nmap failed: {' '.join(cmd)}\n{proc.stderr.strip()}")


def parse_open_tcp_ports(xml_path: str) -> List[Tuple[int, str]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ports: List[Tuple[int, str]] = []
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
        ports.append((int(port_id), service))

    ports.sort(key=lambda x: x[0])
    return ports


def build_basic_html_report(html_path: str, target: str, ports: List[Tuple[int, str]]) -> None:
    rows = []
    for port, service in ports:
        rows.append(f"<tr><td>{port}</td><td>{html.escape(service)}</td><td>open</td></tr>")

    table_rows = "\n".join(rows) if rows else "<tr><td colspan='3'>No open TCP ports found</td></tr>"

    html_content = f"""<!DOCTYPE html>
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

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)


def create_html_report(xml_path: str, html_path: str, target: str, ports: List[Tuple[int, str]]) -> str:
    # Preferred method from the lab material.
  try:
    proc = run_cmd(["xsltproc", xml_path, "-o", html_path])
    if proc.returncode == 0:
      return "xsltproc"
  except FileNotFoundError:
    pass

    # Fallback if xsltproc is unavailable.
    build_basic_html_report(html_path, target, ports)
    return "python-fallback"


def main() -> int:
    parser = argparse.ArgumentParser(description="Full TCP scan with HTML report generation")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--basename", default="target", help="Output base filename (default: target)")
    args = parser.parse_args()

    target = args.target
    base = args.basename

    run_full_scan(target, base)

    xml_path = f"{base}.xml"
    html_path = f"{base}.html"
    if not os.path.exists(xml_path):
        raise FileNotFoundError(f"Expected XML output was not found: {xml_path}")

    open_ports = parse_open_tcp_ports(xml_path)
    method = create_html_report(xml_path, html_path, target, open_ports)

    highest_port = max((p for p, _ in open_ports), default=None)

    print(f"Target: {target}")
    print(f"Output files: {base}.nmap, {base}.gnmap, {base}.xml, {base}.html")
    print(f"HTML generation: {method}")
    print(f"Open TCP ports: {', '.join(str(p) for p, _ in open_ports) if open_ports else 'None'}")
    print(f"Highest open TCP port: {highest_port if highest_port is not None else 'None'}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
