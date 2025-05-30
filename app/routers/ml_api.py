from fastapi import APIRouter, Body

from app.models.request_model import AnalyzeMLRequest
from app.models.response_model import BaseResponse, AnalyzeMLResponse
from app.services.ml_analyzer_service import ml_predict

router = APIRouter(prefix="/analyze", tags=["ML Analyzer"])


@router.post("/ml", response_model=BaseResponse)
def analyze_with_ml(req: AnalyzeMLRequest = Body(...)):
    prediction, confidence = ml_predict(req.numbers, req.top_k)
    return BaseResponse(
        success=True,
        message="ML-based analysis successful.",
        data=AnalyzeMLResponse(
            prediction=prediction,
            confidence=confidence,
            model="RuleFreeML-v1"
        )
    )
