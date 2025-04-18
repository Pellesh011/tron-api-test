from pydantic import BaseModel

class TonAddressRequest(BaseModel):
    trx:str

class TonHistoryRequest(BaseModel):
    limit: int
    offset: int


class TonRequestHistoryBase(BaseModel):
    trx: str
    balance: int
    energy: int
    bandwidth: int

class TonRequestHistoryBaseCreate(TonRequestHistoryBase):
    pass

class TonRequestHistory(TonRequestHistoryBase):
    id: int

    class ConfigDict:
        from_attributes =  from_attributes=True
