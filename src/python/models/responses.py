from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from core.database import Base


class Response(Base):
    __tablename__ = "responses"

    numerical_answer = Column(Integer, nullable=True)
    string_answer = Column(Text, nullable=True)
    answer_of = Column(
        Integer, ForeignKey("questionnaire_questions.id", ondelete="CASCADE"), nullable=False
    )
