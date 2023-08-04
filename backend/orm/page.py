from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from camada_banco import Base

# Classe para representar a tabela 'pages' do banco de dados
class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  # Restrição única no campo name
    tags = relationship('Tag', secondary='count_tags')