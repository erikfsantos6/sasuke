# Calculadora simples com match-case

# Solicita entradas do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Estrutura match-case para verificar o operador
match operador:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero!"
    case _:
        resultado = "Operador inválido!"

# Exibe os dados
print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print(f"Operador: {operador}")
print(f"Resultado: {resultado}")