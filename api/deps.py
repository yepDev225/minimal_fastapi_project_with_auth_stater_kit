from fastapi import Depends
from jose import jwt, JWTError
from core import config, security
from db.session import sessionlocal
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from models.models import User

oauth_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token") #add a token generation route path
token_dependency = Annotated[str, Depends(oauth_bearer)]

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session, Depends(get_db)]


def get_current_user(db:db_dependancy, token:token_dependency)->User:
    credentials = ValueError("unauthorized, you need to be connected")
    try:
        decode_token = jwt.decode(token, config.settings.SECRET_KEY, algorithms=[security.settings.ALGORITHM]) 
    except JWTError:
        raise credentials
    else:
        importante_user_field = decode_token.get("sub")
        user_id = decode_token.get("id")
        user_role = decode_token.get("role")
        if importante_user_field is None or user_id is None or user_role is None:
            raise credentials
        #get_user_in_db
        #user = db.query(User).filter(User.id == user_id).first()
        user = {}
        if not user:
            raise credentials
        return user


user_dependancy = Annotated[User, Depends(get_current_user)]