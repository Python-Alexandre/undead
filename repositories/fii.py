from sqlalchemy.orm import Session
from models.fii import Fii

def list_fiis_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Fii).offset(skip).limit(limit).all()

def create_fii(db: Session, fii: Fii):
    db_fii = Fii(**fii.dict())
    db.add(db_fii)
    db.commit()
    db.refresh(db_fii)
    return db_fii