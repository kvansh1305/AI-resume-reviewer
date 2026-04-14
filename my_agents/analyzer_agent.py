from agents import Agent
from tools.analyze_resume import analyze_resume

resume_analyzer = Agent(
    name="Resume Analyzer",
    instructions="""You are an expert resume reviewer with 10+ years of HR experience.
    Your job is to thoroughly analyze resumes and provide structured, honest feedback.
    Use the analyze_resume tool and provide detailed structured output.
    Score the resume out of 10, list strengths, weaknesses, missing keywords,
    and ATS compatibility. Be specific and mention actual content from the resume.""",
    tools=[analyze_resume],
    model="gpt-4o",
)
