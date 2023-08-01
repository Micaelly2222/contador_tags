# importando a biblioteca 're'(regex), que será usada para fazer a análise do código HTML
import re
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from data_access import insert_page_data, get_page_info
import os

app = FastAPI()

# função para ler o conteúdo do arquivo "index.html"
def read_index_html():
    # Obtem o caminho absoluto para o diretório "frontend"
    frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")

    #  caminho absoluto para o arquivo "index.html"
    index_html_path = os.path.join(frontend_dir, "public", "index.html")

    # Lê o conteúdo do arquivo "index.html"
    with open(index_html_path) as f:
        content = f.read()

    return content


# definindo a função para processar a página e contar as tags HTML
def count_tags(html_code):
    # inicializa um dicionário vazio para armazenar as contagens de cada tag encontrada
    tags_count = {}
    # utilizei a função 'findall' do módulo 're' para procurar todas as ocorrências de tags HTML no código da página
    # a expressão re '<(\w+)' busca por padrões de texto que começam com '<', seguido de uma ou mais letras, números ou underscore (\w+)
    # os parênteses em '(\w+)' agrupam o conteúdo da tag (nome da tag) para que possa acessar posteriormente
    tags = re.findall(r'(\w+)', html_code)


    # for sobre a lista de tags encontradas
    for tag in tags:
        # incrementa a contagem da tag no dicionário 'tags_count'
        # se a tag já estiver no dicionário, a função 'get' retorna o valor correspondente a tag, caso contrário, retorna 0
        # somam 1 a contagem atual da tag e atualiza o valor no dicionário
        tags_count[tag] = tags_count.get(tag, 0) + 1

    # retorna o dicionário com as contagens de cada tag
    return tags_count



# rota para exibir a página HTML do editor do Mônaco
@app.get("/", response_class=HTMLResponse)
async def read_editor():
    content = read_index_html()
    return HTMLResponse(content=content)

# rota para pesquisar as tags de um determinado HTML usando o Mônaco
@app.post("/search_tags")
async def search_tags(html_code: str):
    # processa o código HTML e conta as tags
    tags_count = count_tags(html_code)

    return {"tags_count": tags_count}

# rota para subir um novo HTML usando o editor do Mônaco
@app.post("/upload_html")
async def upload_html(file: UploadFile = File(...)):
    # Lê o conteúdo do arquivo HTML
    html_code = await file.read()

    # processa o código HTML e conta as tags
    tags_count = count_tags(html_code)

    # onsere os dados da página no banco de dados
    page_name = file.filename
    insert_page_data(page_name, tags_count)

    return {"message": "Página e tags inseridas com sucesso!"}
