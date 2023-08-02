from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from controller import count_tags
from data_access import insert_page_data, get_page_info

app = FastAPI()

# Classe para receber o código HTML e nome da requisição
class HTMLRequest(BaseModel):
    html_name: str
    html_code: str

# Rota para pesquisar as tags de um determinado HTML (GET)
@app.get("/search_tags")
async def search_tags(html_code: str):
    tags_count = count_tags(html_code)
    return {"tags_count": tags_count}

# Rota para subir um novo HTML e contar as tags (POST)
@app.post("/upload_html")
async def upload_html(request: HTMLRequest):
    html_name = request.html_name
    html_code = request.html_code
    tags_count = count_tags(html_code)
    page_id = insert_page_data(html_name, tags_count)
    return {"message": "Página e tags inseridas com sucesso!", "page_id": page_id}

# Rota para obter as informações de uma página pelo nome (GET)
@app.get("/get_page_info/{page_name}")
async def get_page_info_by_name(page_name: str):
    page_info = get_page_info(page_name)
    return {"page_info": page_info}
