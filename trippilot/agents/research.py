from trippilot.state import TravelState
from trippilot.tools.web import web_research

def destination_agent(state: TravelState):
    result = web_research(
        f"destination attractions practical travel information: {state['user_request']}"
    )
    return {"research": {"destination": result}}

def stay_agent(state: TravelState):
    result = web_research(
        f"hotels neighborhoods activities travel planning: {state['user_request']}"
    )
    research = dict(state.get("research", {}))
    research["stay_and_activities"] = result
    return {"research": research}
