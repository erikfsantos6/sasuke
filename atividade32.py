import os
os.system("cls")

vetor = [0] * 5  # Cria um vetor com 5 posições, todas iniciadas em 0

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor < 0:
        vetor[i] = 0
    else:
        vetor[i] = valor

print("Valores no vetor:", vetor)
