class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print("-" * 30)

    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}")


# Lista para armazenar as pessoas
pessoas = []

# === Cadastro usando laço de repetição ===
for i in range(3):
    print(f"\n--- Cadastro da pessoa {i + 1} ---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")
    
    pessoa = Pessoa(nome, cpf, telefone)
    pessoas.append(pessoa)

# === Exibir todos os dados ===
print("\n=== DADOS COMPLETOS ===")
for p in pessoas:
    p.mostrar_dados()

# === Exibir dados de SMS marketing ===
print("\n=== TELEFONES PARA SMS MARKETING ===")
for p in pessoas:
    p.dados_sms_marketing()
