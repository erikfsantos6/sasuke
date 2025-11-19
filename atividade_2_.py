from dataclasses import dataclass
import os
import csv

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")


# ---------------- FUNÇÕES -------------------------------------

def ler_idade():
    """Garante que a idade digitada seja válida."""
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade não pode ser negativa!")
                continue
            return idade
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def cadastrar_pacientes(qtd):
    """Cadastra pacientes e retorna lista."""
    lista = []
    for i in range(qtd):
        print(f"\nCadastro {i+1}/{qtd}")

        nome = input("Digite seu nome: ").strip()
        idade = ler_idade()

        lista.append(Paciente(nome, idade))
    return lista


def salvar_csv(arquivo, lista_pacientes):
    """Salva lista no CSV e adiciona cabeçalho caso o arquivo não exista."""
    arquivo_existe = os.path.exists(arquivo)

    with open(arquivo, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Se o arquivo não existir ainda, adiciona cabeçalho
        if not arquivo_existe:
            writer.writerow(["Nome", "Idade"])

        for paciente in lista_pacientes:
            writer.writerow([paciente.nome, paciente.idade])


def exibir_pacientes(lista):
    print("\n=== Lista de Pacientes ===")
    for paciente in lista:
        paciente.exibir_dados()


# ---------------- PROGRAMA PRINCIPAL ----------------------------

def main():
    QUANTIDADE = 2
    arquivo = "dados_pacientes.csv"

    pacientes = cadastrar_pacientes(QUANTIDADE)
    salvar_csv(arquivo, pacientes)
    exibir_pacientes(pacientes)


if __name__ == "__main__":
    main()


