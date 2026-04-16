"""HTTP helpers for lab status pages and content fetches."""

from __future__ import annotations

import re
import urllib.request
from typing import Dict, Optional, Tuple


def fetch_url(url: str, method: str = "GET", timeout: int = 10) -> Tuple[str, Dict[str, str]]:
    request = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8", errors="ignore")
        headers = {key: value for key, value in response.headers.items()}
        return body, headers


def get_alert_count(target: str, timeout: int = 10) -> Optional[int]:
    body, _ = fetch_url(f"http://{target}/status.php", timeout=timeout)
    match = re.search(r"Recorded alerts:\s*(\d+)\s*/\s*\d+\s*alerts", body, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None
