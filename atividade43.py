# Classe Cliente com os dados pedidos
class Cliente:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    # Função que mostra dados de entrega
    def dados_entrega(self):
        print("=== Dados para Entrega ===")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print("---------------------------")

    # Função que mostra dados de email marketing
    def dados_email_marketing(self):
        print("=== Dados para E-mail Marketing ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print("---------------------------")


# Programa principal
cliente1 = Cliente("Erik Silva", "erik@email.com", "Rua das Flores, 123")

# Chamando as funções
cliente1.dados_entrega()
cliente1.dados_email_marketing()
