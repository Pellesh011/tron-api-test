from fastapi import FastAPI
from .db.db import  engine, Base
from .api.v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/v1")

async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 

@app.on_event("startup")
async def startup_event():
    await create_database()