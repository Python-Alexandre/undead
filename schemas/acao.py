from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class AcaoBase(BaseModel):
    papel: str
    data_coleta: datetime

class AcaoCreate(AcaoBase):
    cotacao: float
    pl: float
    pvp: float
    psr: float
    dividend_yield: float
    p_ativo: float
    p_cap_giro: float
    p_ebit: float
    p_ativ_circ_liqs: float
    ev_ebit: float
    ev_ebitda: float
    mrg_ebit: float
    mrg_liq: float
    roic: float
    roe: float
    liq_corr: float
    liq_2_meses: float
    patrim_liq: float
    div_brut_patrim: float
    cresc_rec_5_a: float

class AcaoUpdate(BaseModel):
    papel: Optional[str] = None
    data_coleta: Optional[datetime] = None

class AcaoResponse(AcaoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # necessário para SQLAlchemy
