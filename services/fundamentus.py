from sqlalchemy.orm import Session
from repositories.acao import list_acoes as repo_list_acoes

def list_acoes(db: Session, skip: int = 0, limit: int = 10):
    return repo_list_acoes(db, skip, limit)
