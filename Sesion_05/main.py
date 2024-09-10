from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from enum import Enum
from sqlalchemy.orm import Session

from app.v1.model.model import UserModel
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

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    city: str
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]

@app.get('/')
async def root():
    return {"name": "Henry Colonia"}

@app.get('/posts/{id}')
async def getPost(id):
    return {"data": id}

@app.post('/posts')
async def viewPost(post: Post):
    return {"alert" : f"El post de {post.title} ha sido agregado a la biblioteca"}

@app.post('api/v1/add_user')
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('api/v1/users/{id}')
def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return

@app.get('/api/v1/users')
def get_all_users():
    return db

@app.put('api/v1/users/{id}')
def update_user(id: UUID, user_update: UpdateUser):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id

@app.post('/api/v1/users', response_model = UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(id=uuid4(), first_name=user.first_name, last_name=user.last_name, city=user.city)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



db: List[User] = [
    User(
        id=uuid4(),
        first_name="Henry",
        last_name="Colonia",
        city="Lima",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Javier",
        last_name="Moya",
        city="Callao",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Juan",
        last_name="Moya",
        city="Ica",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Maria",
        last_name="Moy",
        city="Huancayo",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Esther",
        last_name="Perez",
        city="Huaral",
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Ernesto",
        last_name="Mori",
        city="Cusco",
        roles=[Role.user, Role.admin]
    )
]