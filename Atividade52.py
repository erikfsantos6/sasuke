import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 5
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: "))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "w") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome},{aluno.idade}\n")
print("Salvo com sucesso!")
