# services/job_matcher.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()  # ✅ Load environment variables from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-70b-8192"

if not GROQ_API_KEY:
    raise ValueError("🚨 GROQ_API_KEY is not set. Check your .env file!")

print("🔑 GROQ_API_KEY loaded successfully.")

def build_prompt(resume: str, job: str) -> str:
    return f"""
You are an expert career advisor AI.

Given the resume and job description below, analyze them and strictly follow this format in your response:

---

**1. Match Percentage (only a number between 0 and 100, do NOT include % sign):**  
<number>

**2. Top 3 Strengths:**  
1. <...>  
2. <...>  
3. <...>

**3. Top 3 Missing or Weak Areas:**  
1. <...>  
2. <...>  
3. <...>

**4. Overall Resume Feedback:**  
<paragraph of actionable feedback>

**5. Suggested Skills or Improvements:**  
- <skill or suggestion>  
- <skill or suggestion>

---

Resume:
{resume}

Job Description:
{job}
"""

def get_groq_response(prompt: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful resume analyst AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.4
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ Groq Error", response.status_code)
        print("Response:", response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
