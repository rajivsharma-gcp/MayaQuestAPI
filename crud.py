"""."""
from sqlalchemy.orm import Session

import models
import schema
import random


def get_choices(db: Session, question_id: int):
    """."""
    return db.query(models.Choices).filter(
        models.Choices.q_id == question_id).all()


def get_question(db: Session, quest_id: int):
    return db.query(models.Questions).filter(
        models.Questions.id == quest_id).first()


def get_topics(db: Session, skip: int = 0, limit: int = 100):
    topics = db.query(models.Topics).offset(skip).limit(limit).all()
    return topics


def start_quest(db: Session, topic_id: int):
    questions = [i[0] for i in db.query(models.Questions).with_entities(
        models.Questions.id, models.Questions.choices).filter(
            models.Questions.topic_id == topic_id).all()]
    selected_questions = random.sample(questions, 20)
    # session['questions'] = lst
    return {"questions": selected_questions}
