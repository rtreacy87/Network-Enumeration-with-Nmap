#!/usr/bin/env python3
"""CLI wrapper for the scan-and-report task."""

import sys

from nmap_lab_tools.tasks import cli_scan_and_report


if __name__ == "__main__":
    try:
        raise SystemExit(cli_scan_and_report())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
