from sqlalchemy import Column, Integer, String, UniqueConstraint
from camada_banco import Base

# Classe para representar a tabela 'tags' do banco de dados
class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String, nullable=False, unique=True)  # Restrição única no campo tag