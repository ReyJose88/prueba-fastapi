from fastapi import FastAPI
from app.core.middleware import ResponseTimeMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router
from app.core.config import settings

app = FastAPI(
        title="Prueba técnica", 
        version="1.0"
    )

app.add_middleware(ResponseTimeMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1)