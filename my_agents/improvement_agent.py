from agents import Agent
from tools.suggest_improvements import suggest_improvements

improvement_agent = Agent(
    name="Improvement Agent",
    instructions="""You are an expert resume writer and career coach.
    Your job is to take analysis results and produce concrete, actionable rewrites.
    Use the suggest_improvements tool.
    Provide a rewritten summary, improved bullet points, skills to add,
    formatting tips, and tailored advice.
    When past feedback is provided, build on it and don't repeat the same advice.""",
    tools=[suggest_improvements],
    model="gpt-4o",
)
