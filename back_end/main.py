from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localsession
from schemas import UserData, UserId
from models import Base 

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localsession()
    try:
       yield db
    finally:
       db.close()

@app.get('/')
def root():
  return 'Hi, im API'

@app.get('/api/Users/', response_model=list[UserId])
def get_users(db: Session = Depends(get_db)):
   return crud.get_users(db=db)
