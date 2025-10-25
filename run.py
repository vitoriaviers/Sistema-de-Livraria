from app.app import app 
from app.database import db 

from app.models.livraria_models import LivroModel


with app.app_context():
    db.create_all()
    print("Sucesso na criação de tabelas!")

if __name__ == '__main__':
    # Roda o servidor Flask.
    app.run(debug=True)