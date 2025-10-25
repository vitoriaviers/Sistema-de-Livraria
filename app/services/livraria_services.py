from app.database import db
from app.models.livraria_models import LivroModel
from app.dtos.livraria_dtos import LivroCreateDTO

#Crias as principais funções da nossa livraria
class LivroService:
    def create(self, livro_dto: LivroCreateDTO) -> LivroModel:
        novo_livro = LivroModel(
            titulo=livro_dto.titulo,
            preco=livro_dto.preco,
            categoria=livro_dto.categoria,
            autor=livro_dto.autor
        )
        try:
            db.session.add(novo_livro)
            db.session.commit()
            return novo_livro
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao criar livro no Banco de Dados: {e}")

    def buscar_id(self, livro_id: int) -> LivroModel:
        livro = db.session.get(LivroModel, livro_id)
        if not livro:
            raise Exception(f"ID {livro_id} não encontrada!")
        return livro

    def listar_livros(self) -> list[LivroModel]:
        return db.session.execute(db.select(LivroModel)).scalars().all()

    def update(self, livro_id: int, livro_dto: LivroCreateDTO) -> LivroModel:
        livro = self.buscar_id(livro_id)
        livro.titulo = livro_dto.titulo
        livro.preco = livro_dto.preco
        livro.categoria = livro_dto.categoria
        livro.autor = livro_dto.autor
        try:
            db.session.commit()
            return livro
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao atualizar o livro no Banco de Dados: {e}")

    def delete(self, livro_id: int) -> bool:
        livro = self.buscar_id(livro_id)
        try:
            db.session.delete(livro)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao deletar livro do Banco de Dados: {e}")
