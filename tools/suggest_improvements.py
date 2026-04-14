from agents import function_tool
from typing import List

@function_tool
def suggest_improvements(
    resume_text: str,
    analysis: str,
    past_feedback: str = ""
) -> str:
    """Suggests concrete rewrites and improvements based on analysis.
    Uses past_feedback from memory to give personalized advice.
    Returns improvement suggestions as text."""
    return f"Generating improvements based on analysis."
