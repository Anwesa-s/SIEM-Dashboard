from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.api import ingest, events
from app.api import alerts

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SIEM Dashboard ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ingest.router)
app.include_router(events.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "SIEM backend running"}