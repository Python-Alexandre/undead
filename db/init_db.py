from sqlalchemy import text
from db.session import engine
from db.base import Base

# Importar TODOS os models aqui
# Isso garante que o SQLAlchemy registre as tabelas
from models.acao import Acao
from models.fii import Fii

def init_db() -> None:
    
    print("📦 Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("✅ Banco inicializado com sucesso!")
