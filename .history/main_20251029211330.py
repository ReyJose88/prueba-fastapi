from fastapi import FastAPI

app = FastAPI()
app.title = "Prueba técnica"
app.version = "1.0"

@app.get('/', tags=['Home'])
def home():
    return {1: 33}

@app.get('/prueba', tags=['Home'])
def home():
    return {1: 33}