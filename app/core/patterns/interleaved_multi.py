from __future__ import annotations

from app.core.patterns.arithmetic import analyze_arithmetic
from app.core.patterns.fibonacci import analyze_fibonacci
from app.core.patterns.geometric import analyze_geometric
from app.core.patterns.prime import analyze_prime
from app.core.patterns.second_order import analyze_second_order


def analyze_interleaved_multi(numbers: list[int], count: int) -> dict | None:
    n = len(numbers)
    if n < 6:
        return None

    interleave_base = [
        analyze_prime,
        analyze_arithmetic,
        analyze_geometric,
        analyze_fibonacci,
        analyze_second_order,
    ]
    max_groups = min(5, n // 2 + 1)
    results = []
    for group_count in range(2, max_groups + 1):
        groups = [[] for _ in range(group_count)]
        for i, v in enumerate(numbers):
            groups[i % group_count].append(v)

        sub_patterns = []
        sub_preds = []
        for grp in groups:
            matched = False
            for f in interleave_base:
                res = f(grp, 1)
                if res and res.get("next_number"):
                    sub_patterns.append(res["pattern"])
                    sub_preds.append(res["next_number"])
                    matched = True
                    break
            if not matched:
                break

        if len(sub_patterns) == group_count:
            combined = []
            for i in range(count):
                g = i % group_count
                combined.append(sub_preds[g][0])
            results.append({
                "group_count": group_count,
                "pattern": f"interleaved_{group_count}_way",
                "sub_patterns": sub_patterns,
                "next_number": combined[:count]
            })
    for r in results:
        if r["group_count"] == count and len(r["next_number"]) == count:
            return r
    if results:
        return results[0]
    return None
