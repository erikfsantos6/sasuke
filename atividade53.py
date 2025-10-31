import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 4
lista_livros = []

print("=== Cadastro de Livros ===")

for i in range(QUANTIDADE_LIVROS):
    print(f"\nLivro {i+1}:")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor: ")
    categoria = input("Digite a categoria: ")
    preco = float(input("Digite o preço: R$ "))

    livro = Livro(nome, autor, categoria, preco)
    lista_livros.append(livro)

print("\nSalvando dados...")

arquivo = "catalogo_livros.txt"

with open(arquivo, "w", encoding="utf-8") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, R${livro.preco:.2f}\n")

print("Dados salvos com sucesso no arquivo 'catalogo_livros.txt'!")
