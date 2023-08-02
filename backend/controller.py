import re
from typing import Dict
from data_access import insert_page_data, get_page_info

# funcao para processar o código HTML e contar as tags
def count_tags(html_code: str) -> Dict[str, int]:
    tags_count = {}
    tags = re.findall(r'<(\w+)', html_code)
    for tag in tags:
        tags_count[tag] = tags_count.get(tag, 0) + 1
    return tags_count
