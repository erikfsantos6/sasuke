from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco  # Relacionamento com a classe Endereco


# Exemplo de uso:
endereco1 = Endereco(logradouro="São Vicente", numero=21)
pessoa1 = Pessoa(nome="Neymar junior", idade=36, endereco=endereco1)

print(pessoa1)
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"Endereço: {pessoa1.endereco.logradouro}, {pessoa1.endereco.numero}")
