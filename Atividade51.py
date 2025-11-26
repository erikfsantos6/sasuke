import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: int
    matricula: int
    endereco: str 

    # Método movido para DENTRO da classe
    def mostrar_resultado(self):
        print(f"\n--- Dados do Funcionário ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Admissão: {self.data_de_admissao}")
        print(f"Matrícula: {self.matricula}")
        print(f"Endereço: {self.endereco}\n")

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: int
    endereco: str 

    # Método movido para DENTRO da classe
    def mostrar_resultado(self):
        print(f"\n--- Dados do Cliente ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_de_nascimento}")
        print(f"Endereço: {self.endereco}\n")

lista_funcionario = []
lista_cliente = [] 

for i in range(3,0,-1):
    tentativa_atual=4-i
    print(f"\n------cadastro{tentativa_atual} de 3") 
    print(f"(tentativas restantes: {i})")
#voce cria uma variavel:tentativa_atual=4-i e nos print é so adiciona em contagem de pc é sempre 1 numero a mais
# no for i in range voce segue a logica da contagem (3,0-1 e o -1 é pra diminuir as tentativas)

    try:
        # print(f'\n-------cadastro {i+3} de 3----')

        pergunta = input("Você deseja cadastrar (funcionario) ou (cliente)? [ou 'sair' para encerrar]: ").lower().strip()
        
        if pergunta == 'sair':
            break # Encerra o programa

        # --- BLOCO DO FUNCIONÁRIO ---
        if pergunta == 'funcionario':
            # Removi o 'continue' e o loop for(3) para simplificar. 
            # Agora ele entra neste bloco e executa.
            novo_funcionario = Funcionario(
                nome=input("Digite seu nome: "),
                data_de_admissao=int(input("Digite sua data de admissão (apenas números): ")),
                matricula=int(input("Digite sua matrícula: ")),
                endereco=input("Digite seu endereço: ")
            )
            
            lista_funcionario.append(novo_funcionario)
            novo_funcionario.mostrar_resultado() # Chama o método corretamente

        # --- BLOCO DO CLIENTE ---
        elif pergunta == 'cliente':
            novo_cliente = Cliente(
                nome=input("Digite seu nome: "),
                data_de_nascimento=int(input("Digite sua data de nascimento (apenas números): ")),
                endereco=input("Digite seu endereço: ")
            )
            
            # Correção: Adiciona o CLIENTE na lista, não o funcionário
            lista_cliente.append(novo_cliente)
            novo_cliente.mostrar_resultado()

        else:
            print("Opção inválida. Digite 'funcionario' ou 'cliente'.")

    except ValueError:
        print("\n[ERRO] Você digitou texto num campo de número. Tente novamente.\n")
