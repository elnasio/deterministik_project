from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_fibonacci(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    if all(numbers[i] + numbers[i - 1] == numbers[i + 1] for i in range(1, len(numbers) - 1)):
        a, b = numbers[-2], numbers[-1]
        result = []
        for _ in range(max(1, count)):
            a, b = b, a + b
            result.append(b)
        return {
            PATTERN: "fibonacci",
            NEXT_NUMBER: result
        }

    return None
