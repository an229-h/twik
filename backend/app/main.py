from fastapi import FastAPI

from app import models
from app.auth import router as auth_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hariom IoT API"
)

app.include_router(
    auth_router,
    prefix="/api",
    tags=["Authentication"]
)

@app.get("/")
def root():
    return {
        "status": "running"
    }
