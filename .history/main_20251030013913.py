from fastapi import FastAPI
from app.core.middleware import ResponseTimeMiddleware

app = FastAPI()
app.title = "Prueba técnica"
app.version = "1.0"
app.add_middleware(ResponseTimeMiddleware)

@app.get('/', tags=['Home'])
def home():
    return {1: 33}

@app.get('/prueba', tags=['Home'])
def home():
    return {1: 33}