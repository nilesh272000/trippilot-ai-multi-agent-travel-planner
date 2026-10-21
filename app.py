from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from trippilot.graph import build_graph

app = FastAPI(title="TripPilot AI", version="1.0.0")
templates = Jinja2Templates(directory="templates")
graph = build_graph()

class TravelRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "ok", "service": "trippilot-ai"}

@app.post("/api/travel")
def travel(payload: TravelRequest):
    result = graph.invoke({"user_request": payload.message})
    return {
        "plan": result.get("final_plan", ""),
        "research": result.get("research", {}),
        "itinerary": result.get("itinerary", "")
    }
