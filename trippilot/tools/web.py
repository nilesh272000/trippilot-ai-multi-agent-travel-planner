import os
from dotenv import load_dotenv

load_dotenv()

def web_research(query: str) -> str:
    key = os.getenv("TAVILY_API_KEY")
    if not key:
        return "Web research unavailable: TAVILY_API_KEY is not configured."
    from tavily import TavilyClient
    result = TavilyClient(api_key=key).search(query=query, max_results=5)
    return "\n".join(
        f"- {item.get('title', 'Untitled')}: {item.get('content', '')[:500]}"
        for item in result.get("results", [])
    )
