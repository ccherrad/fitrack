from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from core.database import Base


class Questionnaire(Base):
    __tablename__ = "questionnaire"

    label = Column(String(32), nullable=False)
    guidelines = Column(Text, nullable=True)
    description = Column(Text, nullable=True)


class Question(Base):
    __tablename__ = "questions"

    label = Column(String(32), nullable=False)
    stem  = Column(Text, nullable=True)


class QuestionnaireQuestion(Base):
    __tablename__ = "questionnaire_questions"

    questionnaire_id = Column(
        Integer, ForeignKey(Questionnaire.id, ondelete="CASCADE"), nullable=False
    )
    question_id = Column(
        Integer, ForeignKey(Question.id, ondelete="CASCADE"), nullable=False
    )
