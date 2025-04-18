import pytest
from ..db.models import TonRequestHistoryModel
from ..services.ton_service import TonService
from .common.db import AsyncSessionLocal
from .common.client import client, test_db

@pytest.mark.asyncio
async def test_create_request(client):
    async with AsyncSessionLocal() as session:
        ton_service = TonService(session)
        item = TonRequestHistoryModel(trx='test', balance=11110, energy=11110, bandwidth=1000)
        res = await ton_service.create_request(item)
        assert res.trx == "test"

@pytest.mark.asyncio
async def test_get_request(client):
    async with AsyncSessionLocal() as session:
        ton_service = TonService(session)
        res = await ton_service.get_requests()
        assert res[len(res) - 1].trx == "test"


