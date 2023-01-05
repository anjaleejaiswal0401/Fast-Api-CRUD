from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from newapi import api as newapiRoute
from configs.connection import DATABASE_URL 



db_url = DATABASE_URL()
 

app = FastAPI()

app.include_router(newapiRoute.router, prefix="/newapi", tags=["newapi"]),

register_tortoise(
    app,
    db_url=db_url,
    modules={'models': ['newapi.models','aerich.models']},
    generate_schemas=True,
    add_exception_handlers=True
)