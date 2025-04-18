from fastapi import APIRouter
from .ton.ton import router as v1_router

api_router = APIRouter()

api_router.include_router(v1_router, prefix="/ton", tags=["ton"])
