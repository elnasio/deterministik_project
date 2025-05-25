from __future__ import annotations


def analyze_digit_compression(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 3:
        return None

    compressed = []
    for n in numbers:
        digits = list(map(int, str(n)))
        if len(digits) < 2:
            return None
        compressed.append(sum(digits))

    diffs = [compressed[i + 1] - compressed[i] for i in range(len(compressed) - 1)]
    if len(set(diffs)) == 1:
        step = diffs[0]
        last_digits = list(map(int, str(numbers[-1])))
        base = sum(last_digits)
        result = [base + step * (i + 1) for i in range(max(1, count))]
        return {
            "pattern": "digit_compression_sum",
            "digit_sum_step": step,
            "next_number": result
        }

    return None
