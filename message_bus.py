from typing import Dict, Optional
import queue
import threading

class MessageBus:
    """Communication channel between agents"""
    def __init__(self):
        self.queues: Dict[str, queue.Queue] = {}
        self.lock = threading.Lock()

    def register_agent(self, agent_id: str):
        with self.lock:
            if agent_id not in self.queues:
                self.queues[agent_id] = queue.Queue()

    def send_message(self, from_agent: str, to_agent: str, message: dict):
        if to_agent in self.queues:
            self.queues[to_agent].put({"from": from_agent, "content": message})

    def get_message(self, agent_id: str, timeout: float = 1.0) -> Optional[dict]:
        try:
            return self.queues[agent_id].get(timeout=timeout)
        except queue.Empty:
            return None