from sqlalchemy import Column, Integer, String, BigInteger
from .db import Base

class TonRequestHistoryModel(Base):
    __tablename__ = "ton_request_history"

    id = Column(Integer, primary_key=True, index=True)
    trx = Column(String, nullable=False)
    balance = Column(BigInteger, nullable=False)
    energy = Column(BigInteger, nullable=False)
    bandwidth = Column(BigInteger, nullable=False)
