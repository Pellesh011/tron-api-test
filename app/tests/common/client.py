import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from typing import AsyncGenerator

from .db import engine, AsyncSession, AsyncSessionLocal
from app.db.db import get_db
from app.main import app, Base

pytestmark = pytest.mark.asyncio


@pytest_asyncio.fixture(scope="module")
async def test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session 

app.dependency_overrides[get_db] = override_get_db

@pytest_asyncio.fixture(scope="module")
def client(test_db):
    with TestClient(app) as c:
        yield c

