Eu vejo que você quer garantir que o seu `README.md` seja formatado corretamente no GitHub, pois o Markdown (a linguagem usada nos READMEs) requer linhas vazias ou sintaxe especial para pular linhas.

Aqui está o seu conteúdo formatado com **Markdown** e **códigos** para garantir que ele pule as linhas e apareça profissionalmente.

````markdown
# 📚 DESAFIO BACK-END: GERENCIAMENTO DE LIVRARIA

Essa API REST foi desenvolvida em Python sendo utilizada a Framework Flask e o ORM Flask-SQLAlchemy. O MySQL foi o banco de dados escolhido para fazer a gerência dos livros. O projeto se divide em camadas como: controllers, services, models, dtos para deixar o código mais claro. Foi criado com objetivo de atender a segunda fase do processo seletivo da empresa júnior Asci.

---

## 🛠️ Como Rodar o Projeto

Para rodar o projeto localmente é preciso ter instalados:
1. Python 3.8+
2. PIP (gerenciador de pacotes do Python)
3. MySQL Server

Depois de instalados, vá para a pasta raiz do projeto (`SISTEMALIVRARIA`) e siga os comandos:

### 1. Configuração do Ambiente Virtual

Primeiro passo é criar o ambiente virtual:
```bash
python -m venv venv
````

Segundo passo é ativarmos o ambiente virtual:

```bash
.\venv\Scripts\Activate
```

Terceiro passo é instalar as dependências do `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2\. Conexão com o Banco de Dados (MySQL)

Para fazer a conexão, vá ao servidor do banco de dados e crie-o:

```sql
CREATE DATABASE sistemalivraria
```

Logo em seguida, crie o arquivo `.env` na raiz do projeto e insira as credenciais de conexão (user, senha, host, porta, nome).

### 3\. Iniciar o Servidor

Para iniciarmos o servidor Flask e criar a tabela `livros`, rode no terminal:

```bash
python run.py
```

Como resultado, será exibido **"Sucesso na criação de tabelas\!"** e o servidor deve iniciar: `* Running on http://127.0.0.1:5000`

-----

## 🧭 Endpoints da API REST (CRUD)

A **URL Base** é `http://127.0.0.1:5000`.

| Método | Endpoint | Descrição | Status de Sucesso Esperado |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/produtos` | Lista todos os livros. | 200 OK |
| **GET** | `/api/produtos/{id}` | Busca livro por ID. | 200 OK ou 404 Not Found |
| **POST** | `/api/produtos` | Cria novo livro. | 201 Created |
| **PUT** | `/api/produtos/{id}` | Atualiza livro. | 200 OK |
| **DELETE**| `/api/produtos/{id}` | Remove livro. | 204 No Content |

```
```

  
