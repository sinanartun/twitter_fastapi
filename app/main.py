from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import sentiment
from sympy import pi
app = FastAPI()

# Configure CORS
origins = [
    "https://twitter.com",
    "http://localhost",
    "http://localhost:8000",
    "https://x.com"
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/pi")
def calpi():
    calpi = pi.evalf(100000)
    return {calpi}

app.include_router(sentiment.router)
