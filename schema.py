from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# class Questions(Base):
#__tablename__ = "Questions"
#id = Column(Integer, primary_key=True)
#question = Column(String)
#choices = relationship("Choices")
#topic_id = Column(Integer, ForeignKey('Topics.id'))


class QuestionsBase(BaseModel):
    question: str


class QuestionsCreate(QuestionsBase):
    pass


class Questions(QuestionsBase):
    id: int
    topic_id: int
    choices: list

    class Config:
        orm_mode = True


# class Choices(Base):
#     __tablename__ = "Choices"
#     q_id = Column(Integer, ForeignKey('Questions.id'))
#     choice = Column(String)
#     choice_type = Column(Integer)
#     answer = Column(Integer)
#     id = Column('id', Integer, primary_key=True)

class ChoicesBase(BaseModel):
    choice: int
    choice_type: int
    answer: int


class ChoicesCreate(ChoicesBase):
    pass


class Choices(ChoicesBase):
    q_id: int
    id: int


class TopicsBase(BaseModel):
    Name: str


class TopicsCreate(TopicsBase):
    pass


class Topics(TopicsBase):
    id: int

    class Config:
        orm_mode = True
