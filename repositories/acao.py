from sqlalchemy.orm import Session
from sqlalchemy import cast, Date
from models.acao import Acao
from datetime import date

def list_acoes_all(db: Session, skip: int = 0, limit: int = 10):
    hoje = date.today()
    return db.query(Acao).filter(
        cast(Acao.data_coleta, Date) == hoje
    ).offset(skip).limit(limit).all()

def create_acao(db: Session, acao: Acao):
    db_acao = Acao(**acao.dict())
    db.add(db_acao)
    db.commit()
    db.refresh(db_acao)
    return db_acao