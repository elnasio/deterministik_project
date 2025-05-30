from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_repeating(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 4:
        return None

    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    def detect_cycle(seq):
        for i in range(1, len(seq) // 2 + 1):
            pattern = seq[:i]
            if pattern * (len(seq) // i) == seq[:i * (len(seq) // i)]:
                return pattern
        return None

    pattern = detect_cycle(diffs)
    if not pattern:
        return None

    current = numbers[-1]
    result = []
    for i in range(max(1, count)):
        current += pattern[i % len(pattern)]
        result.append(current)

    return {
        PATTERN: "repeating_differences",
        "diff_pattern": pattern,
        NEXT_NUMBER: result
    }
