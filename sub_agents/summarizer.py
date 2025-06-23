from google.adk.agents import LlmAgent

summarizer = LlmAgent(
    model="gemini-2.0-flash",
    name="summarizer",
    description="I am the summarizer; I combine multiple summaries into a single, comprehensive report.",
    instruction="As the summarizer, my role is to merge all provided summaries into one coherent, structured report. Inpiut: {search_results}",
    output_key="final_report"
)
