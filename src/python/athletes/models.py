from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from database import Base


class Athlete(Base):
    __tablename__ = "athletes"

    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    dob = Column(Date, nullable=False)
    bio = Column(Text, nullable=True)
