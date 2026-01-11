from sqlalchemy.orm import Session
from models.fii import Fii
from sqlalchemy import cast, Date
from datetime import date

def list_fiis_all(db: Session, skip: int = 0, limit: int = 10):
    hoje = date.today()
    return db.query(Fii).filter(
        cast(Fii.data_coleta, Date) == hoje
    ).offset(skip).limit(limit).all()

def create_fii(db: Session, fii: Fii):
    db_fii = Fii(**fii.dict())
    db.add(db_fii)
    db.commit()
    db.refresh(db_fii)
    return db_fii