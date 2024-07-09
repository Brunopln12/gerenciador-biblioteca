import sys

estante_livros = []

class Livro:
    def __init__(self, autor, titulo, isbn, emprestado=False):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.emprestado = emprestado
    
    @classmethod
    def adicionar_livro(cls, autor, titulo, isbn, emprestado=False):
        novo_livro = cls(autor, titulo, isbn, emprestado)
        estante_livros.append(novo_livro)
        print("\nLivro adicionado!\n")
    
    @classmethod
    def buscar_livro_por_titulo(cls, titulo):
        encontrado = False
        for livro in estante_livros:
            if titulo in livro.titulo:
                print("Livro Encontrado: ")
                print(f"autor: {livro.autor}, titulo: {livro.titulo}, isbn: {livro.isbn}, emprestado: {livro.emprestado}\n")
                encontrado = True
                return livro
        if not encontrado:
            sys.stderr.write("\nLivro não encontrado!!!\n")
            return None
    
    @classmethod
    def listar_todos_livros(cls):
        if not estante_livros:
            sys.stderr.write("\nNão há livros na biblioteca!!!\n")
            return

        for livro in estante_livros:
            print("Livro: ")
            print(f"autor: {livro.autor}, titulo: {livro.titulo}, isbn: {livro.isbn}, emprestado: {livro.emprestado}\n")