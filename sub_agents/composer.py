from google.adk.agents import LlmAgent

composer = LlmAgent(
    model="gemini-2.0-flash",
    name="composer",
    description="Combines summaries into a full report.",
    instruction="Merge all summaries into a coherent, structured report. Input: {final_report}"
)
