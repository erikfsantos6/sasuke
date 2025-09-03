import os
os.system("cls")

# Solicita os dados do usuário
valor_produto = float(input("Digite o valor do produto: R$ "))
print("Escolha a forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento a prazo")
forma = int(input("Opção: "))

# Usando match-case
match forma:
    case 1:
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print("\n--- Pagamento à vista ---")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (até 6x): "))
        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas
            print("\n--- Pagamento a prazo ---")
            print(f"Valor do produto: R$ {valor_produto:.2f}")
            print("Forma de pagamento: a prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total a prazo: R$ {valor_produto:.2f}")
        else:
            print("Quantidade de parcelas inválida. (Máx: 6)")

    case _:
        print("Opção inválida.")
