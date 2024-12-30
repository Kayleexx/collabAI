from scrapybara import Scrapybara
from typing import Dict
import time
from .agent_state import AgentState
from .message_bus import MessageBus
from .utils import setup_logging, save_locally, format_output

class AgentManager:
    """Manage multiple agents and their interactions"""
    def __init__(self, api_key: str):
        self.client = Scrapybara(api_key=api_key)
        self.agents: Dict[str, dict] = {}
        self.states: Dict[str, AgentState] = {}
        self.message_bus = MessageBus()
        self.logger = setup_logging()

    def create_agent(self, agent_id: str, instance_type: str = "small") -> bool:
        try:
            instance = self.client.start(instance_type=instance_type)
            self.agents[agent_id] = {
                "instance": instance,
                "type": instance_type
            }
            self.states[agent_id] = AgentState(agent_id)
            self.message_bus.register_agent(agent_id)
            self.logger.info(f"Agent {agent_id} created successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error creating agent {agent_id}: {str(e)}")
            return False

    def execute_task(self, agent_id: str, task: dict, max_retries: int = 3):
        state = self.states[agent_id]
        instance = self.agents[agent_id]["instance"]
        
        for attempt in range(max_retries):
            try:
                state.update("working", 25 * (attempt + 1))
                
                if task["type"] == "research":
                    result = instance.agent.act(
                        cmd=task["command"],
                        include_screenshot=False
                    )
                    state.output = result.output
                    state.update("completed", 100)
                    return result.output
                    
                elif task["type"] == "write":
                    return save_locally(
                        content=task["content"],
                        filename=task["filename"],
                        directory=task.get("directory", "outputs")
                    )
                
            except Exception as e:
                state.error_count += 1
                state.update("error", 0)
                self.logger.error(f"Attempt {attempt + 1} failed for {agent_id}: {str(e)}")
                if attempt == max_retries - 1:
                    raise e
                time.sleep(2 ** attempt)

    def cleanup(self):
        """Stop all agents and cleanup resources"""
        for agent_id, agent_data in self.agents.items():
            try:
                agent_data["instance"].stop()
                self.logger.info(f"Agent {agent_id} stopped successfully")
            except Exception as e:
                self.logger.error(f"Error stopping agent {agent_id}: {str(e)}")