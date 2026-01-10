from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from services.fundamentus import list_acoes

router = APIRouter()

@router.get("/acoes")
def list_stocks_all(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return list_acoes(db, skip, limit)
