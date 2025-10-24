import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
@dataclass
class Cliente:
    nome: str
    endereco: str



cliente1 = Cliente(nome="Marta", endereco="Rua Melo moraes filho.")
cliente2 = Cliente(nome="João", endereco="Rua FAzenda Grande do Retiro.")

print("\n") 
print("Mostrando apenas os nomes dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Nome: {cliente2.nome}")

print("\n") #
print("Mostrando apenas os endereços dos clientes.")
print(f"Endereço: {cliente1.endereco}")
print(f"Endereço: {cliente2.endereco}")

print("\n") 
print("Mostrando todos os dados dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco}\n")
print(f"Nome: {cliente2.nome}")
print(f"Endereço: {cliente2.endereco}\n")