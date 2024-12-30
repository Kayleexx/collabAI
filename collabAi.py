from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import traceback
import time
from collaborative_agents.agent_manager import AgentManager
from collaborative_agents.formatters import format_research_command, format_markdown_report
from collaborative_agents.utils import format_output

def get_user_input():
    """Get research topic from user"""
    print("\n=== Sup, I'm CollabAI ===")
    topic = input("Enter a research topic (e.g., 'climate change'): ").strip()
    return topic if topic else "climate change"

def main():
    # Load environment variables
    load_dotenv()
    API_KEY = os.getenv("SCRAPYBARA_API_KEY")
    if not API_KEY:
        raise ValueError("API Key not found! Please set it in the .env file.")

    # Initialize agent manager
    manager = AgentManager(API_KEY)

    try:
        # Get user input
        topic = get_user_input()
        
        # Create agents
        print("\nInitializing agents...")
        manager.create_agent("researcher")
        manager.create_agent("writer")
        
        # Research phase
        print(f"\nResearching '{topic}'...")
        research_task = {
            "type": "research",
            "command": format_research_command(topic)
        }
        research_output = manager.execute_task("researcher", research_task)
        print("\nResearch completed. Processing results...")
        
        # Writing phase
        formatted_output = format_markdown_report(
            format_output(research_output),
            {"Topic": topic}
        )
        
        write_task = {
            "type": "write",
            "filename": f"research_report_{int(time.time())}.md",
            "content": formatted_output
        }
        filepath = manager.execute_task("writer", write_task)
        
        if filepath:
            print(f"\nResearch report saved to: {filepath}")
            print("\nPreview of report:")
            print("-" * 50)
            with open(filepath, 'r', encoding='utf-8') as f:
                print(f.read()[:500] + "...\n")
        else:
            print("\nWarning: Failed to save research report")

    except Exception as e:
        print(f"\nError in workflow: {str(e)}")
        traceback.print_exc()
        
    finally:
        print("\nCleaning up resources...")
        manager.cleanup()

if __name__ == "__main__":
    main()