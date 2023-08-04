from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Conexão com o banco de dados usando o SQLAlchemy
engine = create_engine('sqlite:///tags_database.db')
# Criação da classe base para as tabelas do banco de dados
Base = declarative_base()

# Definindo o Sessionmaker
Session = sessionmaker(bind=engine)

# Função para criar a sessão
@contextmanager
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
        print("Fechando conexão com o banco")


