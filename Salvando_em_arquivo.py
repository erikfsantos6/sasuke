import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Paciente:
    nome:str
    idade:int

    def exibir_dados(self):
        print(f"Nome:{self.nome}n\Idade:{self.idade}")

lista_de_paciente = []
Quantidade_de_Paciente = 2

for i in range(Quantidade_de_Paciente):
    Pacientes = Paciente(
        nome = input("informe seu nome: "),
        idade=input("informe sua idade:")
    )
    lista_de_paciente.append(Pacientes)
    print()#pular uma linha 

nome_do_arquivo = "dados_paciente.cvs"
with open(nome_do_arquivo, "a") as arquivos_paciente:
    for paciente in lista_de_paciente:
        arquivos_paciente.write(f"{Paciente.nome},{Paciente.idade}")
        print("Dados salvos com sucesso")

print("n\Exibindo listas de pacientes")
for paciente in lista_de_paciente:
    paciente.exibir_dados                