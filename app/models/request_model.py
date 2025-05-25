from typing import List, Optional

from pydantic import BaseModel


class LearnRequest(BaseModel):
    numbers: List[int]


class AnalyzeRequest(BaseModel):
    numbers: List[int]
    count: int = 1
    degree: Optional[int] = None


# File: app/models/response_model.py
from pydantic import BaseModel
from typing import Any, Optional


class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None


class ValidateRequest(BaseModel):
    numbers: List[int]
    degree: Optional[int] = None
    prediction: List[int]
