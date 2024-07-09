# Gerenciador Biblioteca

## Descrição

O **Gerenciador Biblioteca** é um sistema de gerenciamento de livros e empréstimos. Ele permite adicionar livros à biblioteca, buscar livros por título, listar todos os livros, realizar e gerenciar empréstimos, e devolver livros emprestados. O projeto é desenvolvido utilizando Programação Orientada a Objetos (POO) em Python.

## Funcionalidades

- **Adicionar Livro**: Permite adicionar um novo livro à biblioteca.
- **Buscar Livro**: Permite buscar um livro pelo título.
- **Listar Livros**: Lista todos os livros disponíveis na biblioteca.
- **Realizar Empréstimo**: Registra um empréstimo de livro.
- **Listar Empréstimos**: Lista todos os empréstimos ativos.
- **Devolver Livro**: Permite devolver um livro emprestado.

## Estrutura do Projeto

```
gerenciador_biblioteca/
│
├── biblioteca/
│   ├── __init__.py
│   ├── livros.py
│   └── emprestimos.py
│
├── interface/
│   ├── __init__.py
│   ├── menu.py
│   └── main.py
│
└── README.md
```

- **biblioteca**: Contém os módulos `livros.py` e `emprestimos.py` responsáveis pelo gerenciamento de livros e empréstimos.
- **interface**: Contém os módulos `menu.py` e `main.py` responsáveis pela interface com o usuário e a execução principal do programa.

## Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/seu-usuario/gerenciador_biblioteca.git
    ```

2. Navegue até o diretório do projeto:
    ```
    cd gerenciador_biblioteca
    ```

3. Certifique-se de ter o Python instalado. Recomenda-se utilizar um ambiente virtual:
    ```
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

4. Instale as dependências necessárias (se houver).

## Uso

Execute o script principal:
```
python interface/main.py
```

Siga as instruções do menu para utilizar as funcionalidades do sistema.

## Contato

- **Desenvolvedor**: [Bruno Nascimento](https://www.linkedin.com/in/brunopinholobonascimento/)
