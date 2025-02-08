# FILE: /ai-agent-demo/ai-agent-demo/README.md

# AI Agent Demonstration Project

This project demonstrates an AI agent that utilizes the OpenAI API and supports Retrieval-Augmented Generation (RAG) with Pgvector as the vector database. The agent can query PostgreSQL order data and includes a memory feature for enhanced interactions.

## Project Structure

```
ai-agent-demo
├── src
│   ├── main.py          # Entry point of the application
│   ├── ai_agent.py      # AI agent class with response generation and memory management
│   ├── database.py       # Functions for PostgreSQL database interactions
│   ├── memory.py         # Memory management for the AI agent
│   ├── rag.py            # RAG implementation using Pgvector
│   └── utils.py          # Utility functions for various operations
├── requirements.txt      # Project dependencies
├── config.py             # Configuration settings
└── README.md             # Project documentation
```

## Setup

1. **Install PostgreSQL** (required for `psycopg2`):
    ```bash
    brew install postgresql
    ```

2. **Create and activate virtual environment**:
    - **macOS/Linux**:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3. **Upgrade setuptools and pip**:
    ```bash
    pip install --upgrade setuptools pip
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the AI agent, execute the following command:
```bash
export PYTHONPATH=$(pwd)
python aichat/main.py
```

## AI Agent Functionality

- **Initialization**: The agent can be set up with specific parameters to tailor its responses.
- **Response Generation**: The agent generates responses based on user input, utilizing its trained knowledge base and RAG approach.
- **Memory Management**: The agent can store and retrieve past interactions to enhance user experience.
- **Database Interaction**: The agent can query order data from a PostgreSQL database.
