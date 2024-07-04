from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://address_book.db",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
