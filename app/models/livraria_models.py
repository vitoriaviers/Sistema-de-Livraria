#Criação da tabela de Livros
from app.database import db

class LivroModel(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<LivroModel {self.titulo}>"
