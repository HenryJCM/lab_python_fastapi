import time
from os import access

from django.contrib.auth.password_validation import get_password_validators
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID
from enum import Enum
from sqlalchemy.orm import Session

from app.v1.utils.db import get_db, authenticate_user, create_access_token, get_password_hash
from app.v1.model.model import User
from app.v1.schema.schema import UserCreate, UserOut

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

@app.post("/token")
def  login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrecto",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "Bearer"}



@app.middleware('http')
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-hi-name"] = "Hi Carol Welcome"

    return response

@app.middleware('http')
async def add_process_time_header(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers["X-process-Time"] = str(process_time)
    print("Tiempo de procedimiento: {}".format(process_time))

    return response

@app.post('/api/v1/users', response_model = UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    new_user = User(id=uuid4(), first_name=user.first_name, last_name=user.last_name, city=user.city, username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/all_users/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    list_users = db.query(User).all()   # Obtenemos todos los usuarios
    return list_users

@app.get("/user/{id}")
def read_user(id: UUID, session: Session = Depends(get_db)):
    user = session.query(User).get(id)

    if not user:
        raise HTTPException(status_code=404, detail=f"Usuario con id {id} no se encuentra en DB")

    return user

@app.put("/user/{id}", response_model=UserOut)
def update_user(id: UUID, user_update: UserCreate, session: Session = Depends(get_db)):
    user = session.query(User).get(id)

    if user:
        user.first_name = user_update.first_name
        user.last_name = user_update.last_name
        user.city = user_update.city
        session.commit()

    if not user:
        raise HTTPException(status_code=404, detail=f"Usuario con id {id} no fue encontrado para actualizar")

    return user

@app.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: UUID, session: Session = Depends(get_db)):
    user = session.query(User).get(id)

    if user:
        session.delete(user)
        session.commit()

    if not user:
        raise HTTPException(status_code=404, detail=f"Usuario con id {id} no fue encontrado")

    return user