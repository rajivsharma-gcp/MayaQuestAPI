from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Questions(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    choices = relationship("Choices")
    topic_id = Column(Integer, ForeignKey('Topics.id'))


class Choices(Base):
    __tablename__ = "Choices"
    q_id = Column(Integer, ForeignKey('Questions.id'))
    choice = Column(String)
    choice_type = Column(Integer)
    answer = Column(Integer)
    id = Column('id', Integer, primary_key=True)


class Topics(Base):
    __tablename__ = "Topics"
    id = Column('id', Integer, primary_key=True)
    Name = Column(String)
