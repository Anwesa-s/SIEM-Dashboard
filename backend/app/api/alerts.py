from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Event
from app.rules.correlation import detect_bruteforce

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):

    events = db.query(Event).all()

    alerts = detect_bruteforce(events)

    return alerts