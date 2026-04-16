"""Minimal DNS message helpers for version.bind CHAOS/TXT queries."""

from __future__ import annotations

import random
import socket
import struct
from typing import Optional, Tuple


def _encode_dns_name(name: str) -> bytes:
    parts = name.rstrip(".").split(".")
    encoded = bytearray()
    for part in parts:
        encoded.append(len(part))
        encoded.extend(part.encode("ascii"))
    encoded.append(0)
    return bytes(encoded)


def _build_query(name: str) -> Tuple[int, bytes]:
    transaction_id = random.randint(0, 0xFFFF)
    flags = 0x0100
    header = struct.pack("!HHHHHH", transaction_id, flags, 1, 0, 0, 0)
    question = _encode_dns_name(name) + struct.pack("!HH", 16, 3)  # TXT, CHAOS
    return transaction_id, header + question


def _skip_name(data: bytes, offset: int) -> int:
    while True:
        length = data[offset]
        if length == 0:
            return offset + 1
        if length & 0xC0 == 0xC0:
            return offset + 2
        offset += 1 + length


def _parse_txt_answer(packet: bytes, expected_id: int) -> Optional[str]:
    if len(packet) < 12:
        return None

    transaction_id, flags, qdcount, ancount, _, _ = struct.unpack("!HHHHHH", packet[:12])
    if transaction_id != expected_id or ancount == 0 or (flags & 0x000F):
        return None

    offset = 12
    for _ in range(qdcount):
        offset = _skip_name(packet, offset)
        offset += 4

    for _ in range(ancount):
        offset = _skip_name(packet, offset)
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


def query_dns_version_bind(target: str, timeout: int = 5) -> Optional[str]:
    txid, query = _build_query("version.bind")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(query, (target, 53))
        response, _ = sock.recvfrom(4096)
    return _parse_txt_answer(response, txid)
