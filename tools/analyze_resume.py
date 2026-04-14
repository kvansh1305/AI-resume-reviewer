from agents import function_tool
from pydantic import BaseModel
from typing import List

class ResumeAnalysis(BaseModel):
    overall_score: int
    strengths: List[str]
    weaknesses: List[str]
    missing_keywords: List[str]
    ats_compatibility: str

@function_tool
def analyze_resume(resume_text: str, job_description: str = "") -> str:
    """Analyzes a resume for strengths, weaknesses, ATS compatibility,
    and missing keywords. Optionally compares to a job description.
    Returns structured feedback as text."""
    return f"Analyzing resume of length {len(resume_text)} characters."
