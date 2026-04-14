import asyncio
from agents import Agent, Runner
from my_agents.analyzer_agent import resume_analyzer
from my_agents.improvement_agent import improvement_agent
from memory.memory_store import memory

orchestrator = Agent(
    name="Orchestrator",
    instructions="""You coordinate resume review tasks.
    First hand off to the Resume Analyzer agent to analyze the resume.
    Then pass those results to the Improvement Agent for suggestions.
    Always include any past feedback from memory context in your instructions.""",
    handoffs=[resume_analyzer, improvement_agent],
    model="gpt-4o",
)

async def review_resume(resume_text: str, job_desc: str = "") -> str:
    past = memory.get_context()

    prompt = f"""Please review this resume.

RESUME:
{resume_text}

JOB DESCRIPTION (optional):
{job_desc}

PAST FEEDBACK CONTEXT:
{past if past else 'No previous sessions.'}
"""
    result = await Runner.run(orchestrator, prompt)
    final = result.final_output

    memory.add("user", f"Submitted resume for review. Job: {job_desc[:100] if job_desc else 'None'}")
    memory.add("assistant", final[:500])

    return final
