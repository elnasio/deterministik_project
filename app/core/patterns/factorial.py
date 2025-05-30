from __future__ import annotations

import math

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_factorial(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 2:
        return None

    for i in range(1, len(numbers) + 1):
        if i >= len(numbers):
            return None
        if math.factorial(i) != numbers[i - 1]:
            return None

    start = len(numbers) + 1
    return {
        PATTERN: "factorial",
        NEXT_NUMBER: [math.factorial(start + i) for i in range(max(1, count))]
    }
