from fastapi import FastAPI

from app.routers.api import router as rule_router
from app.routers.ml_api import router as ml_router

app = FastAPI(title="Pattern Learner API")
app.include_router(rule_router)
app.include_router(ml_router)
