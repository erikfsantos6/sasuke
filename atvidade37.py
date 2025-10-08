import os

# Limpa a tela
os.system("cls")

# Função que converte metros em centímetros
def metros_para_centimetros(metros):
    return metros * 100

# Programa principal
print("=== Conversor de Metros para Centímetros ===")
valor_metros = float(input("Digite o valor em metros: "))
resultado = metros_para_centimetros(valor_metros)

print(f"{valor_metros} metros equivalem a {resultado} centímetros.")
