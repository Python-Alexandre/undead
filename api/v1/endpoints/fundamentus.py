from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from services.fundamentus import list_acoes, list_fiis, update_all

router = APIRouter()

@router.get("/acoes")
def list_acoes_all(
    skip: int = 0,
    limit: int = 1000,
    db: Session = Depends(get_db)
):
    return list_acoes(db, skip, limit)

@router.get("/fiis")
def list_fiis_all(
    skip: int = 0,
    limit: int = 1000,
    db: Session = Depends(get_db)
):
    return list_fiis(db, skip, limit)

@router.get("/update")
def update(
    db: Session = Depends(get_db)
):
    return update_all(db)