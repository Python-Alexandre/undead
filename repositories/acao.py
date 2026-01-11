from sqlalchemy.orm import Session
from models.acao import Acao

def list_acoes_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Acao).offset(skip).limit(limit).all()

def create_acao(db: Session, acao: Acao):
    db_acao = Acao(**acao.dict())
    db.add(db_acao)
    db.commit()
    db.refresh(db_acao)
    return db_acao