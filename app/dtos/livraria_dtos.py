# DTO de entrada de dados
class LivroCreateDTO:
    def __init__(self, titulo: str, preco: float, categoria: str, autor: str | None = None):
        # Validações e caso encontre erros lança-os
        if not titulo or categoria is None:
            raise ValueError("Título e categoria são campos obrigatórios!")
        if preco is None:
            raise ValueError("Preço é obrigatório!")
        if preco <= 0:
            raise ValueError("Preço deve ser um valor positivo!")
        
        self.titulo = titulo
        self.preco = preco
        self.categoria = categoria
        self.autor = autor

# DTO de saída de dados
class LivroResponseDTO:
    def __init__(self, id: int, titulo: str, preco: float, categoria: str, autor: str | None = None):
        self.id = id
        self.titulo = titulo
        self.preco = preco
        self.categoria = categoria
        self.autor = autor

    #Método de classe para converter do objeto Model ()
    @classmethod
    def from_model(cls, livro_model):
        """ Cria um DTO a partir de um objeto LivroModel do SQLAlchemy. """
        return cls(
            id=livro_model.id,
            titulo=livro_model.titulo,
            preco=float(livro_model.preco),
            categoria=livro_model.categoria,
            autor=livro_model.autor
        )
        
    # Converte objetos do DTO em um dicionário para resposta JSON do Flask  
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'preco': float(self.preco),
            'categoria': self.categoria,
            'autor': self.autor
        }