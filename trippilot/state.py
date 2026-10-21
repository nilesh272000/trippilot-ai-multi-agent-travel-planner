from typing import TypedDict

class TravelState(TypedDict, total=False):
    user_request: str
    research: dict
    itinerary: str
    final_plan: str
