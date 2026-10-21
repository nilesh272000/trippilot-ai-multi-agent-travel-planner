from trippilot.state import TravelState
from trippilot.llm import ask_llm

def itinerary_agent(state: TravelState):
    prompt = """Create a practical day-by-day travel itinerary.

User request:
{request}

Research:
{research}

Include morning, afternoon, evening, sensible grouping by area,
transport suggestions, approximate budget guidance, and assumptions.
Do not invent live prices or availability.""".format(
        request=state["user_request"],
        research=state.get("research", {})
    )
    return {"itinerary": ask_llm(prompt)}
