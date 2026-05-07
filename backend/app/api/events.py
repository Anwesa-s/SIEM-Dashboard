from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Event

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/events")
def get_events(
    severity: str = None,
    source_ip: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Event)

    if severity:
        query = query.filter(Event.severity == severity)

    if source_ip:
        query = query.filter(Event.source_ip == source_ip)

    events = query.all()

    return [
        {
            "id": e.id,
            "timestamp": e.timestamp,
            "source": e.source,
            "source_ip": e.source_ip,
            "event_type": e.event_type,
            "severity": e.severity,
            "message": e.message
        }
        for e in events
    ]