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
```cd contador_tags```
3. Instale as dependências do frontend:
``` cd frontend```
```npm install```
```pip install -r requirements.txt```
4. Inicie o servidor FastAPI:
``` cd backend```
```uvicorn main:app --reload```
6. Em outro terminal, inicie o servidor de desenvolvimento do React:
```cd frontend```
```npm start```

A aplicação estará disponível no localhost

## Utilização

Ao acessar a aplicação no localhost, você verá um editor de código HTML. Insira o código HTML que deseja analisar e clique no botão "Enviar html e Contar Tags". A aplicação enviará o código HTML para o servidor, que realizará a contagem de tags e exibirá o resultado na tela. E inserirá os dados no banco de dados SQLite.

Já o botão "Obter informações da página",  é responsável por consultar o banco de dados com o nome da página fornecida, e o servidor retornará as informações sobre as tags contidas na página. 

## Exemplo
Considere o código HTML abaixo.

    <html>
        <head>
            <title>Teste prático</title>
        </head>
        <body>
            <h1>Olá</h1>
            <p>Teste 1</p>
            <p>Teste 2</p>
            <p>Teste 3</p>
        </body>
    </html>  
### Resultado:
Contagem de Tags:
{
    "html": 1,
    "head": 1,
    "title": 1,
    "body": 1,
    "h1": 1,
    "p": 3
}

## Estrutura do Projeto

### Backend

- `main.py`: Contém o código principal da API FastAPI, definindo as rotas /upload_html e /get_page_info.
  
- `camada_banco.py`: Contém as configurações para a conexão com o banco de dados SQLite, incluindo a criação da classe das tabelas do banco (Base) e a função para criar a sessão do SQLAlchemy.
  
- `controller.py`: Contém a lógica de negócio da aplicação, incluindo as funções count_tags, upload_html e get_page_info.

- `data_access.py`: Realiza o acesso ao banco de dados SQLite usando o SQLAlchemy. Define as classes Page, Tag e CountTag para representar as tabelas do banco de dados e possui funções para inserir e obter dados do banco.

- - `tags_database.db`: Banco de dados SQLite que armazena as informações sobre as páginas e as contagens de tags.
  
##### Pasta models

- `tags_count.py`: Define o modelo de dados para a resposta da contagem de tags (TagsCount).

- `page_info.py`: Define o modelo de dados para a resposta das informações da página (PageInfo).

- `page_id.py`: Define o modelo de dados para a resposta do ID da página (PageID).

- `html_request.py`: Define o modelo de dados para a requisição do HTML enviado pelo usuário (HTMLRequest).

##### Pasta ORM

- `count_tag.py`: Define a classe CountTag para representar a tabela 'count_tags' do banco de dados usando o SQLAlchemy.

- `page.py`: Define a classe Page para representar a tabela 'pages' do banco de dados usando o SQLAlchemy.

- `tag.py`: Define a classe Tag para representar a tabela 'tags' do banco de dados usando o SQLAlchemy.

### Frontend

- `App.js`: Componente principal da aplicação React, contendo o editor de código HTML e as funções para realizar as chamadas à API backend.
 
- `index.js`: Arquivo de entrada da aplicação React.

- `App.css`: Arquivo de estilização para o componente App.
 
- `index.html`: Página HTML principal que será carregada pelo navegador.

- `axiosInstance.js` : Arquivo contendo a definição da instância do Axios com a URL base da API, utilizada para realizar as chamadas à API backend a partir do frontend da aplicação.

##  Diagrama de Entidade Relacionamento 
É uma representação gráfica do banco de dados utilizado na aplicação. Ele mostra as tabelas, seus atributos (colunas) e os relacionamentos entre as entidades.
O DER do projeto "Contador de Tags" possui as seguintes entidades:
#### Page : Representa uma página HTML e possui os atributos:
- `id`: Chave primária da tabela.
- `name`: Nome da página.
#### Tag: Representa uma tag HTML e possui os atributos:
- `id`: Chave primária da tabela.
- `tag`: Nome da tag HTML.
#### CountTag : Representa a contagem de uma tag em uma página específica e possui os atributos:
- `id`: Chave primária da tabela.
- `page_id`: Chave estrangeira referenciando a tabela "Page", relacionando a contagem à página específica.
- `tag_id`: Chave estrangeira referenciando a tabela "Tag", relacionando a contagem à tag específica.
- `count`: Quantidade de vezes que a tag aparece na página.

As relações entre as entidades são definidas pelas chaves estrangeiras "page_id" e "tag_id". A tabela `CountTag` atua como uma tabela associativa que armazena a contagem de tags em cada página.

## Aplicação:

![image](https://github.com/Micaelly2222/contador_tags/assets/96353855/a42c8adc-7dae-44ff-ab34-17757c126bfa)


