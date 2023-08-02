# Contador de Tags 

O Contador de Tags é uma aplicação web desenvolvida utilizando as tecnologias FastAPI, SQlite, SQLAlchemy e React. Ela permite que o usuário insira um código HTML e conte a quantidade de tags HTML presentes nele. Além disso, a aplicação possui a funcionalidade de enviar o código HTML para o servidor e armazenar a contagem de tags em um banco de dados SQLite.

## Instalação e Execução

Antes de executar a aplicação, certifique-se de ter as seguintes dependências instaladas em sua máquina:

Python (para o servidor FastAPI)
e Node.js (para o frontend React)

Para executar a aplicação, siga os passos abaixo:

1. Clone o repositório para a sua máquina local:
```git clone https://github.com/Micaelly2222/contador_tags.git```
2. Acesse o diretório do projeto:
```cd contador-tags```
3. Instale as dependências do frontend e backend:
``` cd frontend```
```npm install```
```pip install -r requirements.txt```
4. Inicie o servidor FastAPI:
```uvicorn main:app --reload```
5. Em outro terminal, inicie o servidor de desenvolvimento do React:
```cd frontend```
```npm start```

A aplicação estará disponível no localhost

## Utilização

Ao acessar a aplicação no localhost, você verá um editor de código HTML. Insira o código HTML que deseja analisar e clique no botão "Pesquisar Tags". A aplicação enviará o código HTML para o servidor, que realizará a contagem de tags e exibirá o resultado na tela.

Caso deseje armazenar a contagem de tags em um banco de dados, clique no botão "Enviar HTML". O servidor irá receber o código HTML novamente, realizar a contagem de tags e inserir os dados no banco de dados SQLite.

## Estrutura do Projeto

- `main.py`: Contém o código principal da API FastAPI, definindo as rotas `/search_tags` e `/upload_html`.

- `data_access.py`: Realiza o acesso ao banco de dados SQLite usando o SQLAlchemy. Define as classes Page, Tag e CountTag para representar as tabelas do banco de dados e possui funções para inserir e obter dados do banco.
- 
  - `App.js`: Componente principal da aplicação React, contendo o editor de código HTML e as funções para realizar as chamadas à API backend.

  - `index.js`: Arquivo de entrada da aplicação React.

  - `App.css`: Arquivo de estilização para o componente App.
 
  - `index.html`: Página HTML principal que será carregada pelo navegador.

- `tags_database.db`: Banco de dados SQLite que armazena as informações sobre as páginas e as contagens de tags.
