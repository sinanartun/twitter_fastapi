# app/main.py
from fastapi import FastAPI
from .routers import sentiment

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(sentiment.router)
