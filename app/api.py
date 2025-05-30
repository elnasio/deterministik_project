from fastapi import APIRouter, Body

from app.core.constants import *
from app.models.request_model import LearnRequest, AnalyzeRequest, ValidateRequest
from app.models.response_model import BaseResponse
from app.services.learner_service import learner_service

router = APIRouter()


@router.post("/learn", response_model=BaseResponse)
def learn(req: LearnRequest):
    learner_service.learn_sequence(req.numbers)
    return BaseResponse(success=True, message="Sequence learned.")


@router.get("/predict", response_model=BaseResponse)
def predict():
    result = learner_service.predict_next()
    if result is None:
        return BaseResponse(
            success=False,
            message="Unable to predict. Provide a valid arithmetic or second-order sequence.")
    return BaseResponse(success=True, message="Prediction successful.", data=result)


@router.post("/reset", response_model=BaseResponse)
def reset():
    learner_service.reset()
    return BaseResponse(success=True, message="State reset.")


@router.get("/state", response_model=BaseResponse)
def get_state():
    state = learner_service.get_state()
    return BaseResponse(success=True, message="Current state.", data=state)


@router.post("/analyze", response_model=BaseResponse)
def analyze(req: AnalyzeRequest = Body(...)):
    result = learner_service.analyze_sequence(req.numbers, req.count, req.degree)
    if not result.get("next_number"):
        return BaseResponse(success=False, message="Unable to detect pattern.", data=result)
    return BaseResponse(success=True, message="Pattern analysis successful.", data=result)


@router.post("/validate", response_model=BaseResponse)
def validate_sequence(req: ValidateRequest = Body(...)):
    # derive count dari jumlah prediksi user
    count = len(req.prediction)

    # jalankan analisis dengan count tersebut
    analysis = learner_service.analyze_sequence(
        req.numbers,
        count,
        req.degree
    )
    expected = analysis.get("next_number") or []

    # bandingkan list sesuai urutan
    if expected == req.prediction:
        return BaseResponse(
            success=True,
            message="Cocok",
            data={EXPECTED: expected}
        )
    else:
        return BaseResponse(
            success=False,
            message="Tidak cocok",
            data={EXPECTED: expected, PROVIDED: req.prediction}
        )
