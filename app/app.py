import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from .database import db

load_dotenv()

app = Flask(__name__)

#Cria a URL de conexão com o banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USERNAME')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_DATABASE')}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()
    print("Sucesso na criação de tabelas!")

if __name__ == '__main__':
    app.run(debug=True)

from .routes.routes import register_routes 

# Chame a função para anexar as rotas ao objeto 'app'
register_routes(app)