from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    city = Column(String, nullable=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost:5433/inka_company'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)