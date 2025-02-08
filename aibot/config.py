import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    PGVECTOR_URL = os.getenv("PGVECTOR_URL")
    MEMORY_STORAGE_PATH = os.getenv("MEMORY_STORAGE_PATH", "memory.json")
    RAG_MODEL = os.getenv("RAG_MODEL", "gpt-3.5-turbo")