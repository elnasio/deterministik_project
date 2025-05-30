from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_odd(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 2 or not all(n % 2 == 1 for n in numbers):
        return None

    step = numbers[1] - numbers[0]
    if all(numbers[i + 1] - numbers[i] == step for i in range(len(numbers) - 1)):
        return {
            PATTERN: "odd",
            NEXT_NUMBER: [numbers[-1] + step * (i + 1) for i in range(max(1, count))]
        }

    return None
