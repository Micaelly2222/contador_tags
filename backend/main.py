from fastapi import FastAPI
from models.html_request import HTMLRequest
from models.tags_count import TagsCount
from models.page_id import PageID
from models.page_info import PageInfo
from controller import count_tags, upload_html, get_page_info
from camada_banco import get_db

app = FastAPI()

# Rota para subir um novo HTML e contar as tags (POST)
@app.post("/upload_html", response_model=TagsCount)
async def upload_html_endpoint(request: HTMLRequest):
    html_name = request.html_name
    html_code = request.html_code
    with get_db() as session:
        page_id = upload_html(session, html_name, html_code)
        tags_count = count_tags(session, html_code)
        return {"page_id": page_id, "tags_count": tags_count}


# Rota para obter as informações de uma página pelo nome (GET)
@app.get("/get_page_info/{page_name}", response_model=PageInfo)
async def get_page_info_endpoint(page_name: str):
    with get_db() as session:
        page_info = get_page_info(session, page_name)
        return {"page_info": page_info}
