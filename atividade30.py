# Inicializa a lista e os contadores
numeros = []
pares = 0
impares = 0

# Lê 6 números do usuário
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    
    # Verifica se é par ou ímpar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibe os resultados
print("\nNúmeros informados:", numeros)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
