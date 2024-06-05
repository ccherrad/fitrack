from pydantic import BaseModel
from datetime import date
from typing import Optional

class AthleteIn(BaseModel):
    fullname: str
    dob: date
    bio: Optional[str] = None
    group_id: Optional[int] = None

class AthleteUpdate(BaseModel):
    fullname: Optional[str] = None
    dob: Optional[date] = None
    bio: Optional[str] = None
    group_id: Optional[int] = None

class AthleteOut(BaseModel):
    id: int
    fullname: str
    dob: date
    bio: Optional[str] = None
    group_id: Optional[int] = None

    class Config:
        from_attributes = True
