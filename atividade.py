import os
os. system("cls")

idade = int(input("Digite a idade da pessoa: "))

if idade >= 18 and idade <= 65:
    print("É obrigado a votar.")
else:
    print("Não é obrigado a votar.")
