from __future__ import annotations

from app.core.constants import *


def is_perfect_cube(n: int) -> bool:
    root = round(n ** (1 / 3))
    return root ** 3 == n

def analyze_cubic(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Cek apakah semua adalah bilangan kubik
    if not all(is_perfect_cube(n) for n in numbers):
        return None

    # Temukan nilai n untuk masing-masing elemen: n^3 = x → n = x^(1/3)
    roots = [round(n ** (1 / 3)) for n in numbers]

    # Cek apakah roots itu deret aritmatika
    step = roots[1] - roots[0]
    if all(roots[i + 1] - roots[i] == step for i in range(len(roots) - 1)):
        next_roots = [roots[-1] + step * (i + 1) for i in range(max(1, count))]
        return {
            PATTERN: "cubic",
            NEXT_NUMBER: [r ** 3 for r in next_roots]
        }

    return None
