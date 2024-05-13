from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from core.database import Base


class Group(Base):
    __tablename__ = "groups"

    name = Column(String(32), nullable=False)


class Athlete(Base):
    __tablename__ = "athletes"

    fullname = Column(String(32), nullable=False)
    dob = Column(Date, nullable=False)
    bio = Column(Text, nullable=True)
    group_id = Column(
        Integer, ForeignKey(Group.id, ondelete="CASCADE"), nullable=True
    )
    # group = relationship(Group, back_populates="group")

