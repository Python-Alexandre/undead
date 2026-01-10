from sqlalchemy.orm import Session
from repositories.acao import list_acoes_all

def list_acoes(db: Session, skip: int = 0, limit: int = 10):
    return list_acoes_all(db, skip, limit)