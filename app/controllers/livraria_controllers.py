from flask import request, jsonify
from app.services.livraria_services import LivroService
from app.dtos.livraria_dtos import LivroCreateDTO, LivroResponseDTO

livro_service = LivroService()

class LivroController:
#Cria novo livro
    def create(self):
        try:
            data = request.get_json() or {}
            livro_dto = LivroCreateDTO(
                titulo=data.get('titulo'),
                preco=data.get('preco'),
                categoria=data.get('categoria'),
                autor=data.get('autor')
            )
            novo = livro_service.create(livro_dto)
            response_dto = LivroResponseDTO.from_model(novo)
            return jsonify(response_dto.to_dict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

#Lista todos os livros
    def listar_livros(self):
        try:
            livros = livro_service.listar_livros()
            response = [LivroResponseDTO.from_model(l).to_dict() for l in livros]
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

#Busca livro por ID
    def buscar_id(self, livro_id):
        try:
            livro = livro_service.buscar_id(int(livro_id))
            response = LivroResponseDTO.from_model(livro).to_dict()
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 404 if 'não' in str(e).lower() else 500

#Atualiza livro
    def update(self, livro_id):
        try:
            data = request.get_json() or {}
            livro_dto = LivroCreateDTO(
                titulo=data.get('titulo'),
                preco=data.get('preco'),
                categoria=data.get('categoria'),
                autor=data.get('autor')
            )
            atualizado = livro_service.update(int(livro_id), livro_dto)
            response = LivroResponseDTO.from_model(atualizado).to_dict()
            return jsonify(response), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
#Deleta livros
    def delete(self, livro_id):
        try:
            livro_service.delete(int(livro_id))
            return jsonify({'message': 'Livro deletado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500