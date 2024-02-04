from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from routes import user_routes, profile_routes
from . import database

app = FastAPI()
database.create_tables()

app.include_router(user_routes.router, prefix="/api")
app.include_router(profile_routes.router, prefix="/api")
