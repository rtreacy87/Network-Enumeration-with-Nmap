#!/usr/bin/env python3
"""CLI wrapper for the quiet OS task."""

import sys

from nmap_lab_tools.tasks import cli_quiet_os


if __name__ == "__main__":
    try:
        raise SystemExit(cli_quiet_os())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
