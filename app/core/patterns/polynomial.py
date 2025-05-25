from __future__ import annotations


def analyze_polynomial(numbers: list[int], count: int, degree: int | None = None) -> dict | None:
    if degree is None:
        degree = 2  # default jika tidak ditentukan

    if len(numbers) < degree + 1:
        return None

    import numpy as np
    x = np.arange(len(numbers))
    y = np.array(numbers)

    coeffs = np.polyfit(x, y, deg=degree)
    next_x = np.arange(len(numbers), len(numbers) + max(1, count))
    predicted = np.polyval(coeffs, next_x)
    rounded = [int(round(p)) for p in predicted]

    return {
        "pattern": f"polynomial_deg_{degree}",
        "coefficients": coeffs.tolist(),
        "next_number": rounded,
        "source": "polynomial"
    }
