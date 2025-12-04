import os
from dataclasses import dataclass

os.system("cls")



@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar(self):
        print("\n--- Cliente Cadastrado ---")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}\n")


@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def mostrar(self):
        print("\n--- Produto Cadastrado ---")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Lote: {self.lote}")
        print(f"Validade: {self.validade}\n")


lista_clientes = []
lista_produtos = []


def menu():
    print("\n====== MAMÃO COM AÇÚCAR 🍈======")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Produto")
    print("3 - Listar Clientes")
    print("4 - Listar Produtos")
    print("5 - Sair")
    print("===============================")


while True:
    menu()
    opc = input("Escolha uma opção: ").strip()

   

    if opc == "1":
        print("\n*** Cadastro de Cliente ***")

        novo = Cliente(
            nome=input("Nome: "),
            email=input("E-mail: "),
            telefone=input("Telefone: "),
            endereco=input("Endereço: ")
        )

        lista_clientes.append(novo)
        novo.mostrar()

   
    elif opc == "2":
        print("\n*** Cadastro de Produto ***")

        try:
            novo = Produto(
                nome=input("Nome do produto: "),
                quantidade=int(input("Quantidade: ")),
                lote=input("Lote: "),
                validade=input("Validade: ")
            )

            lista_produtos.append(novo)
            novo.mostrar()

        except ValueError:
            print("\n[ERRO] Quantidade precisa ser número!")

   
    # LISTAR CLIENTES
    
    elif opc == "3":
        print("\n=== Lista de Clientes ===")
        if not lista_clientes:
            print("Nenhum cliente cadastrado.\n")
        else:
            for c in lista_clientes:
                c.mostrar()

    
    # LISTAR PRODUTOS
    
    elif opc == "4":
        print("\n=== Lista de Produtos ===")
        if not lista_produtos:
            print("Nenhum produto cadastrado.\n")
        else:
            for p in lista_produtos:
                p.mostrar()

   
    # SAIR
   
    elif opc == "5":
        print("\nEncerrando sistema... Obrigado! 🍈")
        break

    else:
        print("\n[ERRO] Opção inválida! Tente novamente.\n")
