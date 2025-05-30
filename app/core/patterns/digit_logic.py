from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def count_odd_digits(n: int) -> int:
    return sum(1 for d in str(n) if int(d) % 2 == 1)

def edge_digit_product(n: int) -> int:
    s = str(n)
    return int(s[0]) * int(s[-1]) if len(s) > 1 else int(s[0])

def analyze_digit_logic(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Mode 1: jumlah digit ganjil
    odd_counts = [count_odd_digits(n) for n in numbers]
    if len(set(odd_counts)) == 1:
        return {
            "pattern": "constant_odd_digit_count",
            "odd_digit_count": odd_counts[0],
            "next_number": [odd_counts[0]] * count
        }

    # Mode 2: digit ujung × ujung naik
    products = [edge_digit_product(n) for n in numbers]
    diffs = [products[i + 1] - products[i] for i in range(len(products) - 1)]
    if len(set(diffs)) == 1:
        step = diffs[0]
        last = products[-1]
        return {
            PATTERN: "edge_digit_product_growth",
            NEXT_NUMBER: [last + step * (i + 1) for i in range(count)],
            "product_step": step
        }

    return None
