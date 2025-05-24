from __future__ import annotations


def analyze_arithmetic(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 2:
        return None
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    if len(set(diffs)) == 1:
        step = diffs[0]
        return {
            "pattern": "arithmetic",
            "diff": step,
            "next_number": [numbers[-1] + step * (i + 1) for i in range(max(1, count))]
        }
    return None
