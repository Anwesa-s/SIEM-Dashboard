from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.models import Event
from app.parsers.syslog_parser import parse_log

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ingest")
def ingest_log(log: dict, db: Session = Depends(get_db)):

    raw_message = log.get("message", "")

    event_type, severity = parse_log(raw_message)

    event = Event(
        timestamp=datetime.utcnow(),
        source=log.get("source", "unknown"),
        source_ip=log.get("source_ip", "0.0.0.0"),
        event_type=event_type,
        severity=severity,
        message=raw_message,
        raw_log=str(log)
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {"status": "log ingested", "event_id": event.id}