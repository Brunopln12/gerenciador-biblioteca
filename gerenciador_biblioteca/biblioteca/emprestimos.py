import sys

lista_de_emprestimos = []

class Emprestimo:
    def __init__(self, livro, usuario, data_de_devolucao):
        self.livro = livro
        self.usuario = usuario
        self.data_de_devolucao = data_de_devolucao
    
    @classmethod
    def realizar_emprestimo(cls, livro, usuario, data_de_devolucao):
        emprestimo = cls(livro, usuario, data_de_devolucao)
        lista_de_emprestimos.append(emprestimo)
        print("Livro Emprestado: ")
        print(f"titulo: {livro.titulo}, usuario: {usuario}, data_de_devolucao: {data_de_devolucao}\n")
    
    @classmethod
    def listar_emprestimos_ativos(cls):
        if not lista_de_emprestimos:
            sys.stderr.write("\nNão há livros emprestados!!!\n")
            return

        print("Livros Emprestados: ")
        for emprestimo in lista_de_emprestimos:
            print(f"titulo: {emprestimo.livro.titulo}, usuario: {emprestimo.usuario}, data_de_devolucao: {emprestimo.data_de_devolucao}\n")
    
    @classmethod
    def devolver_livro(cls, livro):
        for emprestimo in lista_de_emprestimos:
            if emprestimo.livro == livro:
                lista_de_emprestimos.remove(emprestimo)
                print("Livro devolvido com sucesso.")
                return
        sys.stderr.write("Livro não encontrado.\n")
