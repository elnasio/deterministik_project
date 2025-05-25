from __future__ import annotations


def analyze_interleaved(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 6:
        return None

    even_indexed = numbers[::2]  # indeks 0, 2, 4, ...
    odd_indexed = numbers[1::2]  # indeks 1, 3, 5, ...

    from app.core.patterns import ALL_ANALYZERS

    result_even = None
    result_odd = None

    for analyzer in ALL_ANALYZERS:
        if analyzer.__name__ == "analyze_interleaved":
            continue  # avoid self-recursion
        if not result_even:
            result_even = analyzer(even_indexed, count)
        if not result_odd:
            result_odd = analyzer(odd_indexed, count)
        if result_even and result_odd:
            break

    if result_even and result_odd:
        # gabungkan hasil prediksi secara selang-seling
        even_pred = result_even["next_number"]
        odd_pred = result_odd["next_number"]
        interleaved = []
        for i in range(max(1, count)):
            interleaved.append(even_pred[i % len(even_pred)])
            interleaved.append(odd_pred[i % len(odd_pred)])
        return {
            "pattern": "interleaved",
            "even_pattern": result_even["pattern"],
            "odd_pattern": result_odd["pattern"],
            "next_number": interleaved[:count]  # jika count = jumlah total yang diinginkan
        }

    return None
