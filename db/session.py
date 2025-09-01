from sqlalchemy.orm import sessionmaker
from base import engine


sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()