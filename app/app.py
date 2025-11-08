from fastapi import FastAPI
from .db import Post, create_db_and_tables, create_async_engine
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/goal")
def greeting():
    return {
        "name": "Elie",
        "goal": "I'm coming for you all"
    }

@app.get("/")
def greeting():
    return {
        "name": "Elie",
    }
