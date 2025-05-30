from typing import Any, Optional, List

from pydantic import BaseModel


class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None


class AnalyzeMLResponse(BaseModel):
    prediction: List[int]
    confidence: List[float]
    model: str
