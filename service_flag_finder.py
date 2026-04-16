#!/usr/bin/env python3
"""CLI wrapper for the service flag task."""

import sys

from nmap_lab_tools.tasks import cli_service_flag


if __name__ == "__main__":
    try:
        raise SystemExit(cli_service_flag())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
