**DESAFIO BACK-END: Gerenciamento De Livraria**

    Essa API REST foi desenvolvida em Python sendo utilizada a Framework Flask e o ORM Flask-SQLAlchemy. O MySQL foi o banco de dados escolhido para fazer a gerencia dos livros. O projeto se divide em camadas como: controllers, services, models, dtos para deixar o código mais claro. Foi criado com objetivo de atender a segunda fase do processo seletivo da empresa júnior Ascii. 

**Como rodar o projeto?**

    Para rodar o projeto localmente é preciso ter instalados:
    1. Python 3.8+
    2.PIP (gerenciador de pacotes do Python)
    3.MySQL Server

    Depois de instalados, vá para a pasta raiz do projeto (SISTEMALIVRARIA) e coloque os seguintes comandos:

    Primeiro passo é criar o ambiente virtual:
    *python -m venv venv*

    Segundo passo é ativarmos o ambiente virtual:
    *.\venv\Scripts\Activate*

    Terceiro passo é instalar as dependências do requirements.txt:
    *pip install -r requirements.txt*

    Depois disso é hora de fazer a conexão com o banco de dados, para isso temos que primeiro ir no servidor do banco de dados e criar-lo ao adicionarmos o comando: 
    *CREATE DATABASE sistemalivraria*
    Logo em seguida criar o arquivo .env na raiz do projeto e inserirmos as credenciais de conexão a exemplo do: user, senha, host, porta, nome.

    Para iniciarmos o servidor Flask e criar a tabela livros devemos rodar: *python run.py* no terminal
    Como resultado vai ser exibido "Sucesso na criação de tabelas!" e o servidor deve iniciar ao indicar * Running on http://127.0.0.1:5000

**Os Endpoints da API REST (CRUD):**
    A URL base é http://127.0.0.1:500

    Temos os 5 endpoints que são:
    - GET /api/produtos → lista todos os livros
    - GET /api/produtos/{id} → busca livro por id
    - POST /api/produtos → cria novo livro
    - PUT /api/produtos/{id} → atualiza livro
    - DELETE /api/produtos/{id} → remove livro

    Para sabermos se deu certo devemos ter como stauts:
    - GET /api/produtos → lista todos os livros =  200 OK
    - GET /api/produtos/{id} → busca livro por id = 200 OK ou 404 Not Found
    - POST /api/produtos → cria novo livro = 201 Created
    - PUT /api/produtos/{id} → atualiza livro = 200 OK
    - DELETE /api/produtos/{id} → remove livro = 204 No Content

  
