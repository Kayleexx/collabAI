from datetime import datetime

class AgentState:
    """Track agent state and progress"""
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.status = "initialized"
        self.progress = 0
        self.last_update = None
        self.error_count = 0
        self.output = None

    def update(self, status: str, progress: int = None):
        self.status = status
        if progress is not None:
            self.progress = progress
        self.last_update = datetime.now()

    def __str__(self):
        return f"Agent {self.agent_id}: {self.status} ({self.progress}%)"