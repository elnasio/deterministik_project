from typing import List, Tuple

from app.ml_model import predict_with_model


def ml_predict(numbers: List[int], top_k: int = 1) -> Tuple[List[int], List[float]]:
    """
    Memprediksi kelanjutan deret angka menggunakan model ML internal.

    :param numbers: Deret angka input.
    :param top_k: Jumlah prediksi teratas yang diambil.
    :return: Tuple prediksi dan confidence-nya.
    """
    if len(numbers) == 0:
        return [], []

    prediction, confidence = predict_with_model(numbers, top_k)
    return prediction, confidence
