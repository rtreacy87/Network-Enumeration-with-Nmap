#!/usr/bin/env python3
"""Quietly query a DNS server version over UDP using CHAOS/TXT version.bind.

Usage:
  python3 quiet_dns_version_finder.py 10.129.2.48
"""

import argparse
import random
import re
import socket
import struct
import sys
import urllib.request
from typing import Optional


def encode_dns_name(name: str) -> bytes:
    parts = name.rstrip(".").split(".")
    encoded = bytearray()
    for part in parts:
        encoded.append(len(part))
        encoded.extend(part.encode("ascii"))
    encoded.append(0)
    return bytes(encoded)


def build_query(name: str) -> tuple[int, bytes]:
    transaction_id = random.randint(0, 0xFFFF)
    flags = 0x0100
    qdcount = 1
    ancount = 0
    nscount = 0
    arcount = 0
    header = struct.pack("!HHHHHH", transaction_id, flags, qdcount, ancount, nscount, arcount)
    question = encode_dns_name(name) + struct.pack("!HH", 16, 3)
    return transaction_id, header + question


def skip_name(data: bytes, offset: int) -> int:
    while True:
        length = data[offset]
        if length == 0:
            return offset + 1
        if length & 0xC0 == 0xC0:
            return offset + 2
        offset += 1 + length


def parse_txt_answer(packet: bytes, expected_id: int) -> Optional[str]:
    if len(packet) < 12:
        return None

    transaction_id, flags, qdcount, ancount, _, _ = struct.unpack("!HHHHHH", packet[:12])
    if transaction_id != expected_id:
        return None
    if ancount == 0:
        return None
    if flags & 0x000F:
        return None

    offset = 12
    for _ in range(qdcount):
        offset = skip_name(packet, offset)
        offset += 4

    for _ in range(ancount):
        offset = skip_name(packet, offset)
        rrtype, rrclass, _, rdlength = struct.unpack("!HHIH", packet[offset:offset + 10])
        offset += 10
        rdata = packet[offset:offset + rdlength]
        offset += rdlength

        if rrtype != 16 or rrclass != 3 or not rdata:
            continue

        text_parts = []
        idx = 0
        while idx < len(rdata):
            part_len = rdata[idx]
            idx += 1
            text_parts.append(rdata[idx:idx + part_len].decode("utf-8", errors="ignore"))
            idx += part_len
        return "".join(text_parts)

    return None


def query_dns_version(target: str, timeout: int = 5) -> Optional[str]:
    txid, query = build_query("version.bind")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(query, (target, 53))
        response, _ = sock.recvfrom(4096)
    return parse_txt_answer(response, txid)


def get_alert_count(target: str, timeout: int = 10) -> Optional[int]:
    with urllib.request.urlopen(f"http://{target}/status.php", timeout=timeout) as response:
        body = response.read().decode("utf-8", errors="ignore")
    match = re.search(r"Recorded alerts:\s*(\d+)\s*/\s*75\s*alerts", body, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Quietly identify a DNS server version over UDP")
    parser.add_argument("target", help="Target IP address")
    args = parser.parse_args()

    alerts_before = get_alert_count(args.target)
    version = query_dns_version(args.target)
    alerts_after = get_alert_count(args.target)

    print(f"Target: {args.target}")
    print(f"Alerts before: {alerts_before if alerts_before is not None else 'Unknown'}")
    print(f"DNS version: {version if version else 'Not found'}")
    print(f"Alerts after: {alerts_after if alerts_after is not None else 'Unknown'}")
    if alerts_before is not None and alerts_after is not None:
        print(f"Alert delta: {alerts_after - alerts_before}")

    return 0 if version else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
