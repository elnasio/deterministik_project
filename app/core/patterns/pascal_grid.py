from __future__ import annotations

import math

from app.core.constants import PATTERN, NEXT_NUMBER


def generate_pascal_rows(limit: int) -> list[list[int]]:
    return [[math.comb(r, k) for k in range(r + 1)] for r in range(limit)]

def flatten_rows(rows: list[list[int]]) -> list[int]:
    return [val for row in rows for val in row]

def analyze_pascal_grid(numbers: list[int], count: int) -> dict | None:
    flat_len = len(numbers)

    # Coba cari berapa banyak baris awal yang menghasilkan flatten sama
    for row_count in range(2, 10):
        rows = generate_pascal_rows(row_count)
        flat = flatten_rows(rows)
        if flat[:flat_len] == numbers:
            # Lanjutkan baris selanjutnya
            new_rows = generate_pascal_rows(row_count + count)
            extended_flat = flatten_rows(new_rows)
            next_vals = extended_flat[flat_len:flat_len + count]
            return {
                PATTERN: "pascal_flattened_grid",
                "rows_used": row_count,
                NEXT_NUMBER: next_vals
            }

    return None
