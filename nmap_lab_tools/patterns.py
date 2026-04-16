"""Common text patterns and extractors."""

from __future__ import annotations

import re
from typing import Optional

FLAG_PATTERNS = [
    r"HTB\{[^\r\n}]+\}",
    r"FLAG\{[^\r\n}]+\}",
    r"flag\{[^\r\n}]+\}",
]


def extract_flag(text: str) -> Optional[str]:
    """Return the first flag-like token found in text."""
    for pattern in FLAG_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    return None
