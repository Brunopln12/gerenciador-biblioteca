from interface import Menu
from biblioteca import Livro, Emprestimo
import datetime
while True:
    menu = Menu()
    opcao = menu.exibir_menu_principal()
    novo_livro = Livro()
    emprestar = Emprestimo()
    if opcao == 'a':
        print("-" * 40)
        print("ADICIONAR LIVROS")
        print("-" * 40)
        autor = str(input("Digite o nome do autor: "))
        titulo = str(input("Qual o título deste Livro: "))
        isbn = int(input("Digite o ISBN do Livro: "))
        novo_livro.adicionar_livro(autor, titulo, isbn)
    
    elif opcao == 'b':
        print("-" * 40)
        print("BUSCAR LIVROS")
        print("-" * 40)
        titulo = str(input("Digite o título do Livro que você procura? "))
        novo_livro.buscar_livro_por_titulo(titulo)

    elif opcao == 'l':
        print("-" * 40)
        print("LISTA DE LIVROS")
        print("-" * 40)
        novo_livro.listar_todos_livros()

    elif opcao == 'li':
        print("-" * 40)
        print("LISTA DE EMPRESTIMO")
        print("-" * 40)
        emprestar.listar_emprestimos_ativos()
    
    elif opcao == 'r':
        print("-" * 40)
        print("REALIZAR EMPRESTIMO")
        print("-" * 40)
        titulo = str(input("Digite o título do Livro? "))
        livro_para_adicionar = novo_livro.buscar_livro_por_titulo(titulo)
        livro_para_adicionar['emprestado'] = True # type: ignore
        usuario = str(input("Digite o nome do Cliente: "))
        print("-" * 40)
        print("Data de devolução")
        data = datetime.date(int(input("Digite o ano: ")),int(input("Digite o mês: ")),int(input("Digite o dia: ")))
        print("-" * 40)
        emprestar.realizar_emprestimo(titulo, usuario, data)
    
    elif opcao == 'd':
        print("-" * 40)
        print("DEVOLVER LIVRO")
        print("-" * 40)
        titulo = str(input("Digite o título do Livro? "))
        livro_para_devolver = novo_livro.buscar_livro_por_titulo(titulo)
        livro_para_devolver['emprestado'] = False # type: ignore
        emprestar.devolver_livro(livro_para_devolver)

    elif opcao == 'x':
        print("\n Até a próxima!!! \n")
        break;

    else:
        print("Opção inválida!!!")