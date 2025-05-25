from __future__ import annotations


def analyze_noise_tolerant(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 4:
        return None

    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    # Cek apakah selisih mayoritas sama (toleransi selisih ±1)
    from collections import Counter
    rounded_diffs = [round(d) for d in diffs]
    common_diff, freq = Counter(rounded_diffs).most_common(1)[0]

    if freq >= len(diffs) - 1:
        # Gunakan diff yang dominan
        base = numbers[-1]
        predicted = [base + common_diff * (i + 1) for i in range(max(1, count))]
        return {
            "pattern": "noise_tolerant_arithmetic",
            "dominant_diff": common_diff,
            "confidence": freq / len(diffs),
            "next_number": predicted
        }

    return None
