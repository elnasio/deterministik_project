from typing import List, Tuple
import random


def predict_with_model(numbers: List[int], top_k: int = 1) -> Tuple[List[int], List[float]]:
    """
    Dummy model: memprediksi angka berikutnya secara acak untuk testing.

    :param numbers: Deret angka input.
    :param top_k: jumlah prediksi teratas.
    :return: Tuple (prediksi, confidence).
    """
    if not numbers:
        return [], []

    # contoh prediksi dummy → angka terakhir + 1..top_k
    last_num = numbers[-1]
    predictions = [last_num + i + 1 for i in range(top_k)]

    # confidence dummy antara 0.5 - 1.0
    confidences = [round(random.uniform(0.5, 1.0), 2) for _ in range(top_k)]

    return predictions, confidences