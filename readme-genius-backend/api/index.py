from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Readme-Genius Backend is Live!"}

# Helper for Vercel
handler = Mangum(app)