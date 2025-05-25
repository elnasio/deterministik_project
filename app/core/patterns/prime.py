from __future__ import annotations


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def analyze_prime(numbers: list[int], count: int) -> dict | None:
    # minimal 3 elemen, dan semua harus prime sepenuhnya
    if len(numbers) < 3 or not all(is_prime(n) for n in numbers):
        return None

    next_numbers = []
    current = numbers[-1]
    while len(next_numbers) < max(1, count):
        current += 1
        if is_prime(current):
            next_numbers.append(current)

    return {
        "pattern": "prime",
        "next_number": next_numbers
    }
