from __future__ import annotations


def analyze_power_series(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    # Coba cari basis dan pangkat
    for base in range(2, 20):
        powers = [base ** i for i in range(len(numbers))]
        if powers == numbers:
            next_vals = [base ** (len(numbers) + i) for i in range(max(1, count))]
            return {
                "pattern": f"power_series_base_{base}",
                "next_number": next_vals
            }

    return None
