from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# conexão com o banco de dados usando o SQLAlchemy
engine = create_engine('sqlite:///tags_database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


# classes para representar as tabelas do banco de dados
class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tags = relationship('Tag', secondary='count_tags')


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String, nullable=False)


class CountTag(Base):
    __tablename__ = 'count_tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('pages.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)
    count = Column(Integer, nullable=False)


# criar as tabelas no banco de dados
Base.metadata.create_all(engine)


# função para inserir os dados da página no banco
def insert_page_data(page_name, tags_count):
    session = Session()

    try:
        with session.begin():
            # verifica se a página já existe no banco de dados
            page = session.query(Page).filter_by(name=page_name).first()
            if not page:
                # se a página não existe, criar uma nova instância da classe Page
                page = Page(name=page_name)
                session.add(page)

            # for sobre o dicionário de contagem de tags e inserir os dados no banco de dados
            for tag, count in tags_count.items():
                # verifica se a tag já existe no banco de dados
                tag_obj = session.query(Tag).filter_by(tag=tag).first()
                if not tag_obj:
                    # se a tag não existe, criar uma nova instância da classe Tag
                    tag_obj = Tag(tag=tag)
                    session.add(tag_obj)

                # criar uma nova instância da classe CountTag e associa ela com a página e a tag
                count_tag = CountTag(page_id=page.id, tag_id=tag_obj.id, count=count)
                session.add(count_tag)

        # commit da transação após a inserção dos dados
        session.commit()
    except Exception as e:
        # em caso de erro, fazer o rollback da transação
        session.rollback()
        raise e
    finally:
        session.close()

# função para obter as informações de uma página pelo nome, usando join
def get_page_info(page_name):
    session = Session()

    # obtendo as informações da página e tags usando join 
    page_info = session.query(Tag.tag, CountTag.count).join(Page).join(CountTag).filter(Page.name == page_name).all()

    session.close()

    return page_info


# função para contar as tags em uma página
def count_tags(page_name):
    session = Session()

    try:
        # obtem a página pelo nome
        page = session.query(Page).filter_by(name=page_name).first()

        if page:
            # obtem a contagem de tags da página
            tag_counts = session.query(Tag.tag, CountTag.count).join(CountTag).filter(CountTag.page_id == page.id).all()
            return {tag: count for tag, count in tag_counts}

        return {}
    finally:
        session.close()