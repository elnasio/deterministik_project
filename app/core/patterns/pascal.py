from __future__ import annotations

import math

from app.core.constants import NEXT_NUMBER, PATTERN


def pascal_row(n: int) -> list[int]:
    return [math.comb(n, k) for k in range(n + 1)]

def analyze_pascal(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Cari baris pascal ke-n yang cocok
    for row_index in range(1, 20):  # batas pencarian baris ke-1 sampai 20
        row = pascal_row(row_index)
        if row == numbers:
            result = [pascal_row(row_index + i) for i in range(1, max(1, count) + 1)]
            return {
                PATTERN: "pascal_triangle_row",
                "row_start": row_index,
                NEXT_NUMBER: result
            }

    return None
