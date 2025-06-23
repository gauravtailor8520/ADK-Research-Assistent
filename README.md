# Research Assistant

A modular, agent-based research assistant designed to analyze queries, search for information, summarize findings, and compose comprehensive reports. Built with extensibility in mind, this project leverages LLM agents and integrates with Google search tools for automated research workflows.

## Features

- **Query Analysis**: Breaks down user queries into actionable research tasks.
- **Automated Search**: Uses Google search tools to gather relevant information from the web.
- **Summarization**: Summarizes search results for concise understanding.
- **Report Composition**: Merges summaries into a structured, coherent report.
- **File Writing**: Saves the final report to a file for easy sharing and reference.
- **Modular Sub-Agents**: Each step is handled by a dedicated sub-agent, making the system easy to extend and maintain.

## Project Structure

```
research_assistent/
    __init__.py
    agent.py
    requirements.txt
    sub_agents/
        composer.py
        file_writer.py
        query_analyzer.py
        search_agent.py
        summarizer.py
```

- `agent.py`: Main agent orchestration logic.
- `sub_agents/`: Contains specialized agents for each research step.
- `requirements.txt`: Python dependencies.

## Installation

1. **Clone the repository**
   ```powershell
   git clone <repo-url>
   cd ADK-Project
   ```
2. **Set up a virtual environment**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```powershell
   pip install -r research_assistent/requirements.txt
   ```

## Usage

1. **Configure your environment**
   - Ensure you have access to the required LLM models and Google ADK tools.
   - Set up any necessary API keys or credentials as required by `google.adk`.

2. **Run the agent**
   - Import and use the main agent in your Python script or interactive session:
     ```python
     from research_assistent.agent import SequentialAgent
     # Initialize and use the agent as needed
     ```

## Sub-Agents Overview

- **Query Analyzer**: Parses and interprets user queries.
- **Search Agent**: Performs web searches using Google tools.
- **Summarizer**: Condenses search results into key points.
- **Composer**: Integrates all summaries into a final report.
- **File Writer**: Saves the report to disk.

## Extending the Project

To add new capabilities:
- Create a new sub-agent in `sub_agents/`.
- Register and orchestrate it in `agent.py`.

## Requirements

- Python 3.10+
- Access to Google ADK and LLM models (e.g., Gemini)

## License

This project is for educational and research purposes. See the LICENSE file for more details.

## Acknowledgements

- Built with [Google ADK](https://github.com/google/adk) agent framework.
- Integrates with Google Search and Gemini LLM APIs.
