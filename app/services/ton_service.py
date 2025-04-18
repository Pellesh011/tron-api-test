from typing import List
from sqlalchemy import select
from ..db.models import TonRequestHistoryModel

class TonService:
    def __init__(self, db):
        self.db = db
        pass

    async def get_requests(self, limit:int = 5, offset: int = 0 ) -> List[TonRequestHistoryModel]:
        result = await self.db.execute(
            select(TonRequestHistoryModel).offset(offset).limit(limit)
        )
        return result.scalars().all()

    async def create_request(self, item: TonRequestHistoryModel):
        self.db.add(item)
        await self.db.commit()
        await self.db.refresh(item)
        return item
   
