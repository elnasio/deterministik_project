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
    primes = [n for n in numbers if is_prime(n)]
    if len(primes) >= 3 and all(is_prime(n) for n in numbers if n > 1):
        result = []
        current = numbers[-1]
        while len(result) < max(1, count):
            current += 1
            if is_prime(current):
                result.append(current)
        return {
            "pattern": "prime",
            "next_number": result
        }
    return None
