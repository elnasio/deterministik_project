from __future__ import annotations

from app.core.constants import PATTERN, NEXT_NUMBER


def is_middle_sum_logic(n: int) -> bool:
    s = str(n)
    if len(s) < 3:
        return False
    first = int(s[0])
    last = int(s[-1])
    mid_index = len(s) // 2
    middle = int(s[mid_index])
    return (first + last) == middle

def analyze_digit_middle_logic(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3 or not all(is_middle_sum_logic(n) for n in numbers):
        return None

    # Anggap logika tetap, maka ulang middle rule
    result = []
    for i in range(1, max(1, count) + 1):
        f = int(str(numbers[-1])[0]) + i
        l = int(str(numbers[-1])[-1]) + i
        m = f + l
        composed = int(str(f) + str(m) + str(l))
        result.append(composed)

    return {
        PATTERN: "middle_digit_sum_of_edges",
        NEXT_NUMBER: result
    }
