from fastapi import APIRouter

route = APIRouter()


@route.get("/")
async def hello():
    return "hello word"