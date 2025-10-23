import os
from dataclasses import dataclass

# Limpa o terminal (funciona no Windows)
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")

# Programa principal
def main():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    pessoa = Pessoa(nome, idade, peso, altura)
    print("\n--- Informações da Pessoa ---")
    pessoa.mostrar_informacoes()

if __name__ == "__main__":
    main()


