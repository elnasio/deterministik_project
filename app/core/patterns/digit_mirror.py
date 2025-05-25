from __future__ import annotations


def is_mirror_growth(n: int) -> bool:
    s = str(n)
    half = len(s) // 2
    if len(s) % 2 == 1:
        left = s[:half]
        right = s[half+1:]
    else:
        left = s[:half]
        right = s[half:]
    return left == right[::-1]

def analyze_digit_mirror(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3 or not all(is_mirror_growth(n) for n in numbers):
        return None

    base = len(str(numbers[-1]))
    digit = str(numbers[0])[0]
    result = []

    for i in range(1, max(1, count) + 1):
        size = base + 2 * i
        half = size // 2
        middle = digit * (half)
        mirror = middle + (digit if size % 2 else "") + middle[::-1]
        result.append(int(mirror))

    return {
        "pattern": "digit_mirror",
        "example": mirror,
        "next_number": result
    }
