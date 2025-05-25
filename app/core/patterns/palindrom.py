from __future__ import annotations


def is_numeric_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def analyze_palindrom(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3 or not all(is_numeric_palindrome(n) for n in numbers):
        return None

    # Cari digit tengah (misal: 1 → 3 → 5 → 7)
    base = numbers[-1]
    result = []
    next_num = base + 1
    while len(result) < max(1, count):
        if is_numeric_palindrome(next_num):
            result.append(next_num)
        next_num += 1

    return {
        "pattern": "numeric_palindrome",
        "next_number": result
    }
