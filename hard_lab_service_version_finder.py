#!/usr/bin/env python3
"""CLI wrapper for the hard-lab service version task."""

import sys

from nmap_lab_tools.tasks import cli_hard_lab


if __name__ == "__main__":
    try:
        raise SystemExit(cli_hard_lab())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
