from __future__ import annotations

from app.core.constants import *


def analyze_bit_pattern(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Cek apakah angka biner terdiri dari semua bit 1 (misal: 1, 3, 7, 15, 31, ...)
    if all(bin(n)[2:] == '1' * bin(n).count('1') for n in numbers):
        # Bit panjang terakhir
        last_bits = len(bin(numbers[-1])) - 2  # -2 untuk '0b'
        result = [2 ** (last_bits + i) - 1 for i in range(1, max(2, count) + 1)]
        return {
            PATTERN: "bit_all_ones",
            NEXT_NUMBER: result[:count],
            "bit_length_start": last_bits + 1
        }

    return None
