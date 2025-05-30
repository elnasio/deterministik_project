from __future__ import annotations

from app.core.constants import *


def analyze_debug(numbers: list[int], count: int) -> dict:
    if len(numbers) < 2:
        return {
            PATTERN: "unknown",
            NEXT_NUMBER: None,
            DEBUG_LABEL: {
                "message": "Not enough data to analyze."
            }
        }

    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    level2_diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)] if len(diffs) > 1 else []

    return {
        PATTERN: "unknown",
        NEXT_NUMBER: None,
        DEBUG_LABEL: {
            "diffs": diffs,
            "level2_diffs": level2_diffs,
            "note": "No known pattern matched. Use debug info to create new pattern module."
        }
    }
