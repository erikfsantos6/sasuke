from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")


def main():
    pessoas = []

    print("=== Cadastro de 4 Pessoas ===")
    for i in range(4):
        print(f"\n--- Pessoa {i+1} ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))

        pessoa = Pessoa(nome, idade, peso, altura)
        pessoas.append(pessoa)

    print("\n=== Dados das Pessoas Cadastradas ===")
    for p in pessoas:
        p.mostrar_dados()


if __name__ == "__main__":
    main()
