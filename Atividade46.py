from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

    def mostrar_endereco(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"


@dataclass
class Pessoa:
    nome: str
    email: str
    endereço: Endereco

    def mostrar_dados(self):
        print("\n--- Dados do Usuário ---")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.mostrar_endereco()}")


# Programa principal
def main():
    print("=== Cadastro de Pessoa ===")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")

    endereco = Endereco(logradouro, numero, cidade)
    pessoa = Pessoa(nome, email, endereco)

    pessoa.mostrar_dados()


if __name__ == "__main__":
    main()

