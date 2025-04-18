from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from typing import List
from app.db.models import TonRequestHistoryModel
from app.models.schemas import TonAddressRequest, TonRequestHistory
from app.services.ton_service import TonService
from app.ton.ton_client import TonClient
from app.db.db import get_db

router = APIRouter()



@router.post("/", response_model=TonRequestHistory)
async def create_item(body: TonAddressRequest, db: AsyncSession = Depends(get_db)):
    ton_service = TonService(db=db)
    ton_client = TonClient()
    data_balance = await ton_client.get_tron_address_balance(body.trx)
    data_resources = await ton_client.get_tron_address_resources(body.trx)
    item = TonRequestHistoryModel(trx=data_balance['address'],
                                   balance = data_balance['balance'],
                                   bandwidth=data_resources['TotalNetLimit'],
                                   energy=data_resources['TotalEnergyLimit'])
    return await ton_service.create_request(item)

@router.get("/", response_model=List[TonRequestHistory])
async def read_items(offset: int = 0, limit: int = 5, db: AsyncSession = Depends(get_db)):
    ton_service = TonService(db=db)
    return await ton_service.get_requests(offset=offset, limit=limit)
