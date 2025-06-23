from google.adk.agents import LlmAgent
from google.adk.tools.google_search_tool import google_search

search_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="search_agent",
    description="Searches the web for information on a given topic.",
    instruction="Search the web for relevant information based on the user's query. Input: ",
    tools=[google_search],
    output_key="search_results"
)
