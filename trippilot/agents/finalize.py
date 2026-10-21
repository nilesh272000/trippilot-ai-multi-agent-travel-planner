from trippilot.state import TravelState
from trippilot.llm import ask_llm

def final_agent(state: TravelState):
    prompt = """Create a concise, useful final travel plan.

Request:
{request}

Research:
{research}

Draft itinerary:
{itinerary}

Use sections:
1. Trip summary
2. Recommended plan
3. Stay/location guidance
4. Budget considerations
5. Practical tips
6. Verification note

Clearly distinguish estimates from verified facts.""".format(
        request=state["user_request"],
        research=state.get("research", {}),
        itinerary=state.get("itinerary", "")
    )
    return {"final_plan": ask_llm(prompt)}
