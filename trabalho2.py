class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
# Inicialize uma lista vazia para armazenar os livros
livros = []
# Função para cadastrar um novo livro
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso.")

# Função para listar todos os livros
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")

# Função para buscar um livro pelo título
def buscar_livro(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}")
            return
    print(f"Livro com título '{titulo}' não encontrado.")
import matplotlib.pyplot as plt

# Função para gerar gráfico de quantidade de livros por gênero
def gerar_grafico_generos():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    
    # Criar um dicionário para contar a quantidade de livros por gênero
    generos = {}
    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    # Gerar o gráfico
    plt.bar(generos.keys(), generos.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()
# Cadastrar alguns livros
cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
cadastrar_livro("O Cortiço", "Aluísio Azevedo", "Romance", 3)
cadastrar_livro("A Arte da Guerra", "Sun Tzu", "Estratégia", 7)

# Listar todos os livros cadastrados
listar_livros()

# Buscar um livro pelo título
buscar_livro("Dom Casmurro")

# Gerar gráfico de quantidade de livros por gênero
gerar_grafico_generos()
