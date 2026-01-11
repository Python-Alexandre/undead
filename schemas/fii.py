from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FiiBase(BaseModel):
    papel: str
    data_coleta: datetime

class FiiCreate(FiiBase):
    cotacao: float
    segmento: str
    cotacao: float
    ffo_yield: float
    dividend_yield: float
    pvp: float
    valor_mercado: float
    liquidez: float
    qtd_imoveis: int
    preco_m2: float
    aluguel_m2: float
    cap_rate: float
    vacancia_media: float   

class FiiUpdate(BaseModel):
    papel: Optional[str] = None
    data_coleta: Optional[datetime] = None

class FiiResponse(FiiBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # necessário para SQLAlchemy
