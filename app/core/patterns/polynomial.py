from __future__ import annotations

import numpy as np

from app.core.constants import NEXT_NUMBER, PATTERN


def analyze_polynomial(numbers: list[int], count: int, degree: int | None = None) -> dict | None:
    if degree is None:
        degree = 2
    if len(numbers) < degree + 1:
        return None

    x = np.arange(len(numbers))
    y = np.array(numbers)

    # Fit polynomial
    coeffs = np.polyfit(x, y, deg=degree)

    # Validasi: pastikan poly(x) ≈ y untuk semua titik asli
    fitted = np.polyval(coeffs, x)
    if not all(int(round(f)) == orig for f, orig in zip(fitted, y)):
        return None

    # Jika lolos validasi, baru prediksi
    next_x = np.arange(len(numbers), len(numbers) + max(1, count))
    predicted = np.polyval(coeffs, next_x)
    rounded = [int(round(p)) for p in predicted]

    return {
        PATTERN: f"polynomial_deg_{degree}",
        "coefficients": coeffs.tolist(),
        NEXT_NUMBER: rounded,
        "source": "polynomial"
    }
