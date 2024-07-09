class Menu():
    def exibir_menu_principal(self):
        menu = '''
    ===============================
                MENU
    ===============================
    [a] Adicionar Livro
    [b] Buscar Livro
    [l] Listar Livros da Biblioteca
    [li] Listar Livros Emprestados
    [r] Realizar empréstimo
    [d] Devolver Livro
    [x] Sair

    => '''
        opcao = input(menu).lower()    
        return opcao
