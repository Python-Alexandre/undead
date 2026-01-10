from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    Text,
    DateTime,
    Index
)
from db.base import Base


class Fii(Base):
    __tablename__ = "fiis"

    id = Column(Integer, primary_key=True, index=True)

    papel = Column(Text, nullable=False)
    segmento = Column(Text)
    cotacao = Column(Numeric)
    ffo_yield = Column(Numeric)
    dividend_yield = Column(Numeric)
    pvp = Column(Numeric)
    valor_mercado = Column(Numeric)
    liquidez = Column(Numeric)
    qtd_imoveis = Column(Integer)
    preco_m2 = Column(Numeric)
    aluguel_m2 = Column(Numeric)
    cap_rate = Column(Numeric)
    vacancia_media = Column(Numeric)

    data_coleta = Column(DateTime, nullable=False)

    __table_args__ = (
        Index(
            "idx_fund_fii_papel_data",
            "papel",
            "data_coleta"
        ),
    )
