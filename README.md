# CollabAI

CollabAI is a framework designed to demonstrate multi-agent collaboration on shared tasks. The system allows multiple agents to work towards a common goal by conducting research, writing notes, and generating reports using Scrapybara's API. This also incorporates dynamic communication between agents, scalability for additional tasks, state monitoring, and error recovery mechanisms. Developed as a submission for Scrapybara's Bounty Force.

---

## Features

### 1. **Multi-Agent Communication**
- **Current**: Agents work sequentially (e.g., one agent researches while another writes).
- **Enhanced**: Agents can now exchange information dynamically during the workflow.
  - Example: Agent 2 validates or expands on Agent 1's research before writing.
- **Implementation**: Introduced a shared memory/message-passing mechanism to enable seamless communication.

### 2. **Scalability**
- Support for more than two agents, each performing distinct tasks.
  - Example:
    - **Agent 1**: Researches the topic.
    - **Agent 2**: Writes structured notes.
    - **Agent 3**: Converts notes into Markdown or a PDF report.
- **Orchestration**: Introduced task dependency management between agents for smooth task transitions.

### 3. **Agent State Monitoring**
- Added a real-time logging system to monitor agent states, performance, and progress.
  - Example:
    - **Agent 1**: Research in progress (80%)
    - **Agent 2**: Writing completed.
- Future work: Build a dashboard for better visualization.

### 4. **Error Recovery Mechanisms**
- **Previous Limitation**: Workflow halted if an agent failed.
- **Enhancement**: Introduced fault-tolerant mechanisms.
  - Agents retry failed tasks or allow another agent to take over.

---

## Project Structure

```
collaborative_agents
├── env
├── outputs
│   └── research_notes.txt
├── .env                 # Environment variables (API keys, etc.)
├── .gitignore           # Ignored files and folders
├── agent_activity.log   # Logs for agent state and progress monitoring
├── agent_manager.py     # Manages agent creation and execution
├── agent_state.py       # Tracks the state and tasks of each agent
├── collabAi.py          # Main script for running the framework
├── formatters.py        # Handles formatting of research outputs and reports
├── message_bus.py       # Implements shared memory/message-passing system
├── utils.py             # Utility functions for logging and processing
└── README.md            # Documentation
```

---

## How to Use

### Prerequisites
1. Python 3.8+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the following content:
   ```env
   SCRAPYBARA_API_KEY=your_api_key_here
   ```

### Running the Framework
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/collaborative_agents.git
   cd collaborative_agents
   ```
2. Run the main script:
   ```bash
   python collabAi.py
   ```
3. Follow the prompts to enter a research topic.

### Outputs
- Research results are saved in the `outputs/` directory as `.txt` or `.md` files.
- Logs are stored in `agent_activity.log` for real-time monitoring.

---

## Workflow Details

### Step 1: Research Phase
- Agent 1 collects data based on the provided topic.
- Results are formatted for further processing.

### Step 2: Writing Phase
- Agent 2 writes structured notes based on the research data.
- Markdown or PDF reports are generated.

### Step 3: Multi-Agent Coordination
- Agents communicate via the `message_bus.py` module for task validation and expansion.

---

## Advanced Features

### Dynamic Communication
- Implemented via `message_bus.py`, allowing agents to:
  - Validate outputs.
  - Share partial results dynamically.

### Scalability
- Added support for additional agents.
- Example Task Flow:
  - **Agent 1**: Research.
  - **Agent 2**: Write structured notes.
  - **Agent 3**: Generate and export reports in Markdown or PDF.

### Error Recovery
- Automatic retries for failed tasks.
- Task reallocation to other agents if retries fail.

### State Monitoring
- Logs agent progress and performance in `agent_activity.log`.
- Future Improvement: Add a graphical dashboard for better visualization.

---

## Contribution Guidelines
We welcome contributions to enhance this framework. To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and create a pull request.

---
## Contact
For questions or feedback, reach out at:
- Email: mitalisinha774@gmail.com

