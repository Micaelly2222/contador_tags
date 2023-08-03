from sqlalchemy.orm import Session
from sqlalchemy import exists
from camada_banco import get_db
from orm.count_tag import CountTag
from orm.page import Page
from orm.tag import Tag
from typing import Dict
from sqlalchemy.exc import SQLAlchemyError


# Função para inserir os dados da página no banco
def insert_page_data(page_name, tags_count):
    with get_db() as session:
        try:
            # Inicia uma transação principal
            with session.begin():
                # Verifica se a página já existe no banco de dados
                page = session.query(Page).filter_by(name=page_name).first()
                if not page:
                    # Se a página não existe, criar uma nova instância da classe Page
                    page = Page(name=page_name)
                    session.add(page)

                # Percorre o dicionário de contagem de tags e insere os dados no banco de dados
                for tag, count in tags_count.items():
                    # Verifica se a tag já existe no banco de dados
                    tag_obj = session.query(Tag).filter_by(tag=tag).first()
                    if not tag_obj:
                        # Se a tag não existe, criar uma nova instância da classe Tag
                        tag_obj = Tag(tag=tag)
                        session.add(tag_obj)

                    # Chama o session.begin_nested() para criar um novo ponto de salvamento interno (nested)
                    with session.begin_nested():
                        # Verifica se já existe uma instância da classe CountTag com os mesmos page_id e tag_id
                        count_tag = session.query(CountTag).filter_by(page_id=page.id, tag_id=tag_obj.id).first()
                        if count_tag:
                            # Se já existe, atualiza o valor de count
                            count_tag.count = count
                        else:
                            # Senão, cria uma nova instância da classe CountTag e associa ela com a página e a tag
                            count_tag = CountTag(page_id=page.id, tag_id=tag_obj.id, count=count)
                            session.add(count_tag)

            # Commit da transação principal após a inserção dos dados
            session.commit()
        except SQLAlchemyError as e:
            # Em caso de erro, faz o rollback da transação
            session.rollback()
            raise InsertError("Erro ao inserir dados no banco de dados.") from e


# Função para obter as informações de uma página pelo nome, usando join
def get_page_info(session: Session, page_name: str):
    with get_db() as session:
        # Obtendo as informações da página e tags usando join
        page_info = session.query(Tag.tag, CountTag.count).join(Page).join(CountTag).filter(Page.name == page_name).all()

    return page_info