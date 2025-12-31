from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Readme-Genius is finally ALIVE! 🤖"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# The handler must be here
handler = Mangum(app)