from typing import List

from pydantic import BaseModel


class LearnRequest(BaseModel):
    numbers: List[int]


class AnalyzeRequest(LearnRequest):
    count: int = 1


# File: app/models/response_model.py
from pydantic import BaseModel
from typing import Any, Optional


class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
