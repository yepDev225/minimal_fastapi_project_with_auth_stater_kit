from sqlalchemy import create_engine
from core.config import settings
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(settings.DATABASE_URI, **settings.get_option())
Base = declarative_base()