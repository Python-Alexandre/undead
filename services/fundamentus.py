from sqlalchemy.orm import Session
from repositories.acao import list_acoes_all
from repositories.fii import list_fiis_all

def list_acoes(db: Session, skip: int = 0, limit: int = 10):
    return list_acoes_all(db, skip, limit)

def list_fiis(db: Session, skip: int = 0, limit: int = 10):
    return list_fiis_all(db, skip, limit)