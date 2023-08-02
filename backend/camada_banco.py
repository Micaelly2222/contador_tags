from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Conexão com o banco de dados usando o SQLAlchemy
engine = create_engine('sqlite:///tags_database.db')

# Criação da classe base para as tabelas do banco de dados
Base = declarative_base()

# Função para criar a sessão
def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


