import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.auth.router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI()

origins = [
    os.getenv("FRONTEND_ORIGIN"),  # Get front-end origin from environment variables
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Hello, World!"}