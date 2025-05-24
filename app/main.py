from fastapi import FastAPI

from app.api import router

app = FastAPI(title="Pattern Learner API")
app.include_router(router)
