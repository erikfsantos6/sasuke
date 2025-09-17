import os
os.system("cls")

soma = 0

while True:
    nota = input("Digite uma nota:")
    if nota < 0 or nota > 10:
        print("A nota inválida.")
    else:
        soma += nota
        break    

media = soma / QUANTIDADE_NOTAS

print(F"media: {media}")   