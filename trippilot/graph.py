from langgraph.graph import StateGraph, START, END
from trippilot.state import TravelState
from trippilot.agents.research import destination_agent, stay_agent
from trippilot.agents.itinerary import itinerary_agent
from trippilot.agents.finalize import final_agent

def build_graph():
    g = StateGraph(TravelState)
    g.add_node("destination_research", destination_agent)
    g.add_node("stay_research", stay_agent)
    g.add_node("itinerary", itinerary_agent)
    g.add_node("finalize", final_agent)
    g.add_edge(START, "destination_research")
    g.add_edge("destination_research", "stay_research")
    g.add_edge("stay_research", "itinerary")
    g.add_edge("itinerary", "finalize")
    g.add_edge("finalize", END)
    return g.compile()
