# routes/resume.py

from fastapi import APIRouter, UploadFile, File, Form
from services.pdf_parser import extract_text_from_pdf
from services.job_matcher import build_prompt, get_groq_response
from utils.job_db import JOB_ROLES

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...), job_role: str = Form(...)):
    resume_text = extract_text_from_pdf(file.file)
    job_text = JOB_ROLES.get(job_role, "Job role not found.")

    prompt = build_prompt(resume_text, job_text)
    result = get_groq_response(prompt)

    return {"feedback": result}
