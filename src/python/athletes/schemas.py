from pydantic import BaseModel
from datetime import date
from typing import Optional

class AthleteIn(BaseModel):
    first_name: str
    last_name: str
    dob: date
    bio: Optional[str] = None

class AthleteUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    dob: Optional[date] = None
    bio: Optional[str] = None

class AthleteOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: date
    bio: Optional[str] = None

    class Config:
        from_attributes = True
