import os
from dotenv import load_dotenv

load_dotenv()

def ask_llm(prompt: str) -> str:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        return "LLM key not configured. Add GROQ_API_KEY to .env to generate the AI plan."
    from langchain_groq import ChatGroq
    llm = ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        api_key=key,
        temperature=0.2
    )
    return llm.invoke(prompt).content
