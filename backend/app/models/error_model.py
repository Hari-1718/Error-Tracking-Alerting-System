from pydantic import BaseModel, Field
from datetime import datetime

class ErrorLog(BaseModel):
    api_name: str
    status_code: int
    error_message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_critical: bool = False
