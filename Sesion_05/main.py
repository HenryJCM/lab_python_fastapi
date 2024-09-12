from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from enum import Enum
from sqlalchemy.orm import Session

from app.v1.model.model import User
from app.v1.schema.schema import UserCreate, UserOut
from app.v1.utils.db import get_db

# instanciamos la clase FastAPI
app = FastAPI()

class Post(BaseModel):
    autor: str
    title: str
    content: str

class Role (str, Enum):
    admin = 'admin'
    user = 'user'

@app.get('/')
async def root():
    return {"name": "Henry Colonia"}

@app.get('/posts/{id}')
async def getPost(id):
    return {"data": id}

@app.post('/posts')
async def viewPost(post: Post):
    return {"alert" : f"El post de {post.title} ha sido agregado a la biblioteca"}

@app.post('/api/v1/users', response_model = UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(id=uuid4(), first_name=user.first_name, last_name=user.last_name, city=user.city)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/all_users/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    list_users = db.query(User).all()   # Obtenemos todos los usuarios
    return list_users