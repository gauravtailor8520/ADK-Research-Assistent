from google.adk.agents import LlmAgent

query_analyzer = LlmAgent(
    model="gemini-2.0-flash",
    name="query_analyzer",
    description="Analyzes the user's query to understand the core topic and create a research plan.",
    instruction="Break down the user's query into a list of sub-topics to research. Identify the main entities and concepts. Formulate a step-by-step research plan.",
    output_key="query_analysis",
)
