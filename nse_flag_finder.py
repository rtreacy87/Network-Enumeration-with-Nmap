#!/usr/bin/env python3
"""CLI wrapper for the NSE flag task."""

import sys

from nmap_lab_tools.tasks import cli_nse_flag


if __name__ == "__main__":
    try:
        raise SystemExit(cli_nse_flag())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
