from passlib.context import CryptContext
from jose import jwt
from config import settings
from datetime import datetime, timedelta, timezone


bcrypt_context = CryptContext(schemes = ['bcrypt'], deprecated="auto")

def hash_pwd(pwd:str)->str:
    return bcrypt_context.hash(pwd)

def verify_pwd(pwd:str, hash_pwd:str)->bool:
    try:
        return CryptContext.verify(pwd, hash_pwd)
    except:
        return False

def create_token(user_id, user_role, user_inportante_field):
    payload = {"sub": user_inportante_field, "id": user_id, "role": user_role}
    exp_time =datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({
        "exp": exp_time
    })
    return jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)



