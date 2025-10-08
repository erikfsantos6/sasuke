import os
os.system("cls")

# Função que infla o preço de acordo com o valor informado
def inflacionar_preco(preco):
    if preco < 100:
        novo_preco = preco + (preco * 0.10)  # aumenta 10%
        print("Foi aplicado um aumento de 10%.")
    else:
        novo_preco = preco + (preco * 0.20)  # aumenta 20%
        print("Foi aplicado um aumento de 20%.")
    return novo_preco  # retorna o resultado

# Programa principal
print("=== Cálculo de Inflação de Preço ===")
preco = float(input("Digite o preço do produto: R$ "))
resultado = inflacionar_preco(preco)

print(f"O preço reajustado é: R$ {resultado:.2f}")
