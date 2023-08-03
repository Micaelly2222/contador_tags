import re
from typing import Dict
from collections import Counter
from data_access import insert_page_data, get_page_info

# Função para processar o código HTML e contar as tags
def count_tags(html_code: str) -> Dict[str, int]:
    tags = re.findall(r'<(\w+)', html_code)
    tags_count = Counter(tags)
    return tags_count

# Função para subir um novo HTML e contar as tags
def upload_html(html_name: str, html_code: str):
    tags_count = count_tags(html_code)
    page_id = insert_page_data(html_name, tags_count)
    return page_id

# Função para obter as informações de uma página pelo nome
def get_page_info_by_name(page_name: str):
    page_info = get_page_info(page_name)
    return page_info
