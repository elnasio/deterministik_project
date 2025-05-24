from __future__ import annotations


def analyze_second_order(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    level2_diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]

    if len(set(level2_diffs)) == 1:
        next_numbers = []
        current = numbers[-1]
        current_diff = diffs[-1]
        for _ in range(max(1, count)):
            current_diff += level2_diffs[0]
            current += current_diff
            next_numbers.append(current)
        return {
            "pattern": "second_order",
            "level2_diff": level2_diffs[0],
            "next_number": next_numbers
        }

    return None
