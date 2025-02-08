from ai_agent import AI_Agent
from aibot.config import Config
from aibot.memory import Memory
from aibot.rag import RAG
from aibot.database import Database


def main():
    # Initialize configuration
    config = Config()

    # Initialize the AI agent
    m = Memory()
    db = Database()
    r = RAG(db)
    agent = AI_Agent(api_key=config.OPENAI_API_KEY, memory=m, rag=r)

    # Start the application
    print("AI Agent is running. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = agent.generate_response(user_input)
        print(f"AI Agent: {response}")


if __name__ == "__main__":
    main()
