from __future__ import annotations


def analyze_interleaved_multi(numbers: list[int], count: int) -> dict | None:
    if len(numbers) < 6:
        return None

    from app.core.patterns import ALL_ANALYZERS
    best_result = None

    for group_count in range(2, min(5, len(numbers) // 2 + 1)):
        groups = [[] for _ in range(group_count)]
        for i, val in enumerate(numbers):
            groups[i % group_count].append(val)

        sub_results = []
        for group in groups:
            for analyzer in ALL_ANALYZERS:
                if analyzer.__name__.startswith("analyze_interleaved"):
                    continue
                res = analyzer(group, count)
                if res:
                    sub_results.append(res)
                    break
            else:
                break  # satu grup tidak bisa dianalisis

        if len(sub_results) == group_count:
            # Gabungkan hasil prediksi
            pred = [[] for _ in range(group_count)]
            for i, r in enumerate(sub_results):
                pred[i] = r["next_number"][:count]

            combined = []
            for i in range(count):
                for g in range(group_count):
                    if i < len(pred[g]):
                        combined.append(pred[g][i])

            return {
                "pattern": f"interleaved_{group_count}_way",
                "sub_patterns": [r["pattern"] for r in sub_results],
                "next_number": combined[:count]
            }

    return None
