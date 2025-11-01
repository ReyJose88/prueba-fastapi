from fastapi import FastAPI
from app.core.middleware import ResponseTimeMiddleware

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

app.include_router(api_router, prefix=settings.API_V1_STR)