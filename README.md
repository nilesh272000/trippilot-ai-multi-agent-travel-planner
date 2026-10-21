# ✈️ TripPilot AI — Multi-Agent Travel Planner

A portfolio-oriented, independently implemented multi-agent travel planning assistant built with LangGraph, FastAPI, Groq, and optional Tavily web research.

## Architecture
User Request → Destination Research → Stay & Activity Research → Itinerary Agent → Final Synthesizer

## Features
- Specialized travel-planning agents
- LangGraph orchestration
- Groq-powered synthesis
- Optional Tavily web research
- FastAPI backend
- Browser UI
- Graceful API-key fallbacks
- Health endpoint
- Automated health test

## Run locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app:app --reload --port 8000
```

Open `http://127.0.0.1:8000`.

## Environment variables
See `.env.example`. Never commit real API keys.

## API
- `GET /health`
- `POST /api/travel`

Example body:
```json
{"message":"Plan a 4-day budget trip to Singapore for two people from Mumbai."}
```

## Portfolio note
This is an independent implementation inspired by the general multi-agent travel-planning problem. It is not a copy of any specific repository implementation.

Travel information can change, so users should verify live prices, availability, visa rules, and booking details with official providers.
