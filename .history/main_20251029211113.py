from fastapi import FastAPI

app = FastAPI()
app.title = "Prueba técnica"

@app.get('/')
def home():
    return "Hola pepewwww"