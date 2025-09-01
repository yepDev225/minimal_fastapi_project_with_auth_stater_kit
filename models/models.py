from db.base import Base
from sqlalchemy import Column, INTEGER, String, Enum as SqlalchemyEnum
from enum import Enum

class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER,primary_key=True , index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index= True, unique=True)
    role = Column(SqlalchemyEnum(Role), default=Role.USER)
    password = Column(String)
    ...