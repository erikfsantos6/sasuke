import os
os.system("cls")

# Cardápio fixo com código, nome e valor
cardapio = [
    ["Picanha", 25.00],
    ["Lasanha", 20.00],
    ["Strogonoff", 18.00],
    ["Bife acebolado", 15.00],
    ["Pão com ovo", 5.00]
]


pedidos = []

while True:
    # Exibe o cardápio
    print("\n--- CARDÁPIO ---")
    for i in range(len(cardapio)):
        print(f"{i + 1} - {cardapio[i][0]} - R$ {cardapio[i][1]:.2f}")

    # Solicita a escolha do prato
    try:
        codigo = int(input("Digite o código do prato desejado (1 a 5): "))
        if 1 <= codigo <= 5:
            pedidos.append(codigo - 1)  # Armazena o índice do prato
        else:
            print("Código inválido.")
            continue
    except ValueError:
        print("Entrada inválida.")
        continue

    # Pergunta se deseja continuar
    continuar = input("Deseja pedir outro prato? (s/n): ").lower()
    if continuar != 's':
        break

# Mostra os pedidos
print("\n--- PEDIDOS REALIZADOS ---")
total = 0
for i in pedidos:
    nome = cardapio[i][0]
    preco = cardapio[i][1]
    print(f"{nome} - R$ {preco:.2f}")
    total += preco

print(f"\nTOTAL A PAGAR: R$ {total:.2f}")
