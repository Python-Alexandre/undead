from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FiiBase(BaseModel):
    papel: str
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

class FiiCreate(FiiBase):
    data_coleta: datetime

class FiiUpdate(BaseModel):
    data_coleta: Optional[datetime] = None

class FiiResponse(FiiBase):
    id: int
    data_coleta: datetime

    class Config:
        from_attributes = True  # necessário para SQLAlchemy
