from pydantic import BaseModel
from datetime import datetime

class AuditLogCreate(BaseModel):
    agent_name: str
    model_used: str
    prompt: str
    response: str
    tokens_used: int
    latency_ms: float
    status: str = "SUCCESS"

class AuditLogResponse(AuditLogCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True