import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from data_access import insert_page_data, get_page_info

app = FastAPI()

# classe para receber o código HTML da requisição
class HTMLRequest(BaseModel):
    html_code: str

# funcao para processar o código HTML e contar as tags
def count_tags(html_code: str) -> Dict[str, int]:
    tags_count = {}
    tags = re.findall(r'<(\w+)', html_code)
    for tag in tags:
        tags_count[tag] = tags_count.get(tag, 0) + 1
    return tags_count

# rota para pesquisar as tags de um determinado HTML
@app.post("/search_tags")
async def search_tags(request: HTMLRequest):
    html_code = request.html_code
    tags_count = count_tags(html_code)
    return {"tags_count": tags_count}

# rota para subir um novo HTML e contar as tags
@app.post("/upload_html")
async def upload_html(request: HTMLRequest):
    html_code = request.html_code
    tags_count = count_tags(html_code)
    page_id = insert_page_data(html_code, tags_count)
    return {"message": "Página e tags inseridas com sucesso!", "page_id": page_id}
