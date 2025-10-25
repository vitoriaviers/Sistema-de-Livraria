from ..controllers.livraria_controllers import LivroController 
from flask import request, jsonify

livro_controller = LivroController()

#Função que registra todas as rotas
def register_routes(app_instance):
    """
    Recebe a instância da aplicação Flask (app) e anexa todas as rotas.
    """
    # 1. GET /api/produtos → lista todos os livros
    app_instance.add_url_rule('/api/produtos', 
        view_func=livro_controller.listar_livros, 
        methods=['GET']
    )

    # 2. GET /api/produtos/{id} → busca livro por id
    app_instance.add_url_rule('/api/produtos/<int:livro_id>', 
        view_func=livro_controller.buscar_id, 
        methods=['GET']
    )

    # 3. POST /api/produtos → cria novo livro
    app_instance.add_url_rule('/api/produtos', 
        view_func=livro_controller.create, 
        methods=['POST']
    )

    # 4. PUT /api/produtos/{id} → atualiza livro
    app_instance.add_url_rule('/api/produtos/<int:livro_id>', 
        view_func=livro_controller.update, 
        methods=['PUT']
    )

    # 5. DELETE /api/produtos/{id} → remove livro
    app_instance.add_url_rule('/api/produtos/<int:livro_id>', 
        view_func=livro_controller.delete, 
        methods=['DELETE']
    )
    