from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print("\n--- Dados da Pessoa ---")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

print("Solicitando os dados da pessoa...")

pessoa = Pessoa(
    nome=input("Digite seu nome: "),
    email=input("Digite seu e-mail: "),
    telefone=input("Digite seu telefone: "),
    endereco=input("Digite seu endereço: ")
)

print("\nExibindo dados:")
pessoa.mostrar_dados()
