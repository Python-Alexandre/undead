from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class AcaoBase(BaseModel):
    name: str
    email: EmailStr


class AcaoCreate(AcaoBase):
    password: str


class AcaoUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class AcaoResponse(AcaoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # necessário para SQLAlchemy
