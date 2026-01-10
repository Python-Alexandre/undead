from fastapi import APIRouter
from api.v1.endpoints import fundamentus

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(fundamentus.router, prefix="/fundamentus", tags=["Fundamentus"])
