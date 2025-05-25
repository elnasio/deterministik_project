from __future__ import annotations


def analyze_digit_repetition(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 2:
        return None

    # Ubah angka ke string dan cek pola digit
    patterns = [str(n) for n in numbers]

    def is_repeating_digit_pattern(seq):
        lengths = [len(s) for s in seq]
        if not all(set(s) == {s[0]} for s in seq):  # semua digit harus sama, seperti '1', '11', '111'
            return False
        if not all(lengths[i + 1] - lengths[i] == 1 for i in range(len(lengths) - 1)):
            return False
        return True

    if is_repeating_digit_pattern(patterns):
        digit = patterns[0][0]
        base_len = len(patterns[-1])
        next_numbers = [int(digit * (base_len + i + 1)) for i in range(max(1, count))]
        return {
            "pattern": "digit_repetition",
            "repeated_digit": digit,
            "next_number": next_numbers
        }

    return None
