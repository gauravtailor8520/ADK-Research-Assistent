from google.adk.agents import SequentialAgent
from .sub_agents.query_analyzer import query_analyzer
from .sub_agents.search_agent import search_agent
from .sub_agents.summarizer import summarizer
from .sub_agents.composer import composer

root_agents = SequentialAgent(
    name="coordinator",
    description="Runs agents in order: analyze → search → summarize → compose.",
    sub_agents=[query_analyzer, search_agent, summarizer, composer]
)


root_agent = root_agents