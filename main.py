from fastapi import FastAPI
from models import models
from db.base import engine
from api.v1 import global_route


app = FastAPI()

@app.on_event("startup")
def init_db():
    models.Base.metadata.create_all(bind=engine)


app.include_router(global_route.route)
