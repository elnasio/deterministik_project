from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def is_triangular(n: int) -> bool:
    # Triangular number formula: n(n+1)/2 = x => solve for n
    from math import sqrt
    x = (8 * n + 1)
    root = sqrt(x)
    return root.is_integer()


def analyze_triangular(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Cek apakah semua adalah bilangan segitiga
    if not all(is_triangular(n) for n in numbers):
        return None

    # Temukan n awal
    triangulars = []
    i = 1
    while len(triangulars) < len(numbers) + count:
        t = i * (i + 1) // 2
        triangulars.append(t)
        i += 1

    # Temukan offset (index pertama kemunculan)
    try:
        start_idx = triangulars.index(numbers[0])
        if triangulars[start_idx:start_idx + len(numbers)] == numbers:
            return {
                PATTERN: "triangular",
                NEXT_NUMBER: triangulars[start_idx + len(numbers): start_idx + len(numbers) + max(1, count)]
            }
    except ValueError:
        return None

    return None
