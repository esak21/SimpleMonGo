from pydantic import BaseModel
from  datetime import datetime

class Incident(BaseModel):
    title: str
    description: str
    is_deleted: bool = False
    reported_by: str
    assigned_to: str
    status: str
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))