from __future__ import annotations


def analyze_geometric(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 2 or 0 in numbers:
        return None

    try:
        ratios = [numbers[i + 1] / numbers[i] for i in range(len(numbers) - 1)]
    except ZeroDivisionError:
        return None

    if len(set(ratios)) == 1:
        ratio = ratios[0]
        return {
            "pattern": "geometric",
            "ratio": ratio,
            "next_number": [numbers[-1] * (ratio ** (i + 1)) for i in range(max(1, count))]
        }

    return None
