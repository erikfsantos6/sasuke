import os
from dataclasses import dataclass

# Limpa o terminal (Windows)
os.system("cls")

@dataclass
class Contato:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_informacoes(self):
        print("\n--- Dados do Contato ---")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

# Programa principal
def main():
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")

    contato = Contato(nome, email, telefone, endereco)
    contato.mostrar_informacoes()

if __name__ == "__main__":
    main()
