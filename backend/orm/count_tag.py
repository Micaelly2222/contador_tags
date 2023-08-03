from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from camada_banco import Base

# Classe para representar a tabela 'count_tags' do banco de dados
class CountTag(Base):
    __tablename__ = 'count_tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('pages.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)
    count = Column(Integer, nullable=False)
    UniqueConstraint('page_id', 'tag_id', name='uq_page_tag')  # Restrição única para a combinação page_id e tag_id