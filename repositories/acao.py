from sqlalchemy.orm import Session
from models.acao import Acao

def list_acoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Acao).offset(skip).limit(limit).all()
