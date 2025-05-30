from __future__ import annotations

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_modulo_cycle(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 4:
        return None

    # Cek selisih antar elemen
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    # Coba temukan pola berulang dari hasil modulo
    for mod in range(2, 10):
        mods = [n % mod for n in numbers]
        for i in range(1, len(mods)//2 + 1):
            pattern = mods[:i]
            if pattern * (len(mods) // i) == mods[:i * (len(mods) // i)]:
                # Prediksi berdasarkan angka terakhir + offset (selisih tetap jika ada)
                step = numbers[1] - numbers[0]
                next_values = []
                current = numbers[-1]
                for _ in range(max(1, count)):
                    current += step
                    next_values.append(current)
                return {
                    PATTERN: f"modulo_cycle_mod_{mod}",
                    "mod_pattern": pattern,
                    NEXT_NUMBER: next_values
                }
    return None
