import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import router

app = FastAPI(
    title="fitrack",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Count"],
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "Ok"}
