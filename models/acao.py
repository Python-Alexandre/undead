from sqlalchemy import Column, Integer, Numeric, Text, DateTime, Index
from db.base import Base

class Acao(Base):
    __tablename__ = "acoes"

    id = Column(Integer, primary_key=True, index=True)

    papel = Column(Text, nullable=False)
    cotacao = Column(Numeric)
    pl = Column(Numeric)
    pvp = Column(Numeric)
    psr = Column(Numeric)
    dividend_yield = Column(Numeric)
    p_ativo = Column(Numeric)
    p_cap_giro = Column(Numeric)
    p_ebit = Column(Numeric)
    p_ativ_circ_liqs = Column(Numeric)
    ev_ebit = Column(Numeric)
    ev_ebitda = Column(Numeric)
    mrg_ebit = Column(Numeric)
    mrg_liq = Column(Numeric)
    roic = Column(Numeric)
    roe = Column(Numeric)
    liq_corr = Column(Numeric)
    liq_2_meses = Column(Numeric)
    patrim_liq = Column(Numeric)
    div_brut_patrim = Column(Numeric)
    cresc_rec_5_a = Column(Numeric)

    data_coleta = Column(DateTime, nullable=False)

    __table_args__ = (
        Index(
            "idx_acoes_papel_data",
            "papel",
            "data_coleta"
        ),
    )
