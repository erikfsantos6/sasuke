import os
os.system("cls")

# Programa para calcular o peso ideal

# Entrada de dados
sexo = input("Digite o sexo (M para Masculino / F para Feminino): ").strip().upper()
altura = float(input("Digite a altura em metros: "))

# Cálculo do peso ideal
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido! Use apenas 'M' ou 'F'.")

# Saída
if peso_ideal is not None:
    print(f"O peso ideal é: {peso_ideal:.2f} kg")
 

