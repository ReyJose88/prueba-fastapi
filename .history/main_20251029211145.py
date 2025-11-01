from fastapi import FastAPI

app = FastAPI()
app.title = "Prueba técnica"
app.version = "1.0"

@app.get('/')
def home():
    return "Hola pepewwww"