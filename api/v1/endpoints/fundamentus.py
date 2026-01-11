from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from services.fundamentus import list_acoes, list_fiis, update_acoes_all

router = APIRouter()

@router.get("/acoes")
def list_acoes_all(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return list_acoes(db, skip, limit)

@router.get("/fiis")
def list_fiis_all(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return list_fiis(db, skip, limit)

@router.get("/update_acoes")
def update_acoes(
    db: Session = Depends(get_db)
):
    return update_acoes_all(db)