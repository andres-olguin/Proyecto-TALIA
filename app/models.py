from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from .database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    agent_name = Column(String(100), index=True)
    model_used = Column(String(100))
    prompt = Column(Text)
    response = Column(Text)
    tokens_used = Column(Integer, default=0)
    latency_ms = Column(Float, default=0.0)
    status = Column(String(50), default="SUCCESS")