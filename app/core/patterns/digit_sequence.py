from __future__ import annotations


def is_sequential_digit_growth(n: int) -> bool:
    s = str(n)
    return s == ''.join(str(i) for i in range(1, len(s) + 1))

def analyze_digit_sequence(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3 or not all(is_sequential_digit_growth(n) for n in numbers):
        return None

    last_len = len(str(numbers[-1]))
    result = []

    for i in range(1, max(1, count) + 1):
        seq = ''.join(str(j) for j in range(1, last_len + i + 1))
        result.append(int(seq))

    return {
        "pattern": "digit_sequential_growth",
        "next_number": result
    }
