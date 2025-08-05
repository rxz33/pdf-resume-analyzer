# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.resume import router as ResumeRouter
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

# Now you can access env variables anywhere in your app using os.getenv("VAR_NAME")

app = FastAPI()

# Enable CORS for frontend (React/Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(ResumeRouter, prefix="/api")

@app.get("/")
def root():
    return {"message": "Resume Analyzer API running"}
