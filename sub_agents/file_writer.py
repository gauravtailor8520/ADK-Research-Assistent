from google.adk.agents import LlmAgent

def write_to_file(final_report: str, filename: str = "final_report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_report)
    return f"Report written to {filename}"

file_writer = LlmAgent(
    name="file_writer",
    description="Writes the final report to a file.",
    tools=[write_to_file],  # tools should be a list
    instruction="Write the provided final_report to a file named final_report.txt.",
    input_keys=["final_report"],  # specify the input key
    output_key="file_write_status"
)