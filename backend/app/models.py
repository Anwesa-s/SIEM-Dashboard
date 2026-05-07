from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source = Column(String)
    source_ip = Column(String)
    event_type = Column(String)
    severity = Column(String)
    message = Column(String)
    raw_log = Column(String)