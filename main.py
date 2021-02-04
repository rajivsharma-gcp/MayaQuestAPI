from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import ORJSONResponse

import uvicorn
import crud
import models
import schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"task": "complete"}


@app.get("/get_quest:{quest_id}", response_model=schema.Questions)
def get_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = crud.get_question(db, quest_id=quest_id)
    print(quest)
    return quest


@app.get("/get_topics", response_model=List[schema.Topics])
def get_topics(skip: int = -1,
               limit: int = 100,
               db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip, limit=limit)
    return topics


@app.get("/start_quest:{topic_id}")
def start_quest(topic_id: int, db: Session = Depends(get_db)):
    resp = crud.start_quest(db, topic_id)
    return resp

if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True, debug=True, workers=3)