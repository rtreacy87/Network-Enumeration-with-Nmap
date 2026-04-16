#!/usr/bin/env python3
"""CLI wrapper for the quiet DNS version task."""

import sys

from nmap_lab_tools.tasks import cli_quiet_dns


if __name__ == "__main__":
    try:
        raise SystemExit(cli_quiet_dns())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
