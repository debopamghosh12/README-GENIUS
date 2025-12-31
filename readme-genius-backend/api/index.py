from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Readme-Genius Backend is Live!"}

# This variable MUST be named 'handler'
handler = Mangum(app)