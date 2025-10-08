import os
import time

def somar(a, b):
    resultado = a + b
    print(f"Soma: {a} + {b} = {resultado}")
    time.sleep(2)
    os.system("cls")

def subtrair(a, b):
    resultado = a - b
    print(f"Subtração: {a} - {b} = {resultado}")
    time.sleep(2)
    os.system("cls")

def multiplicar(a, b):
    resultado = a * b
    print(f"Multiplicação: {a} * {b} = {resultado}")
    time.sleep(2)
    os.system("cls")

def dividir(a, b):
    if b != 0:
        resultado = a / b
        print(f"Divisão: {a} / {b} = {resultado}")
    else:
        print("Erro: divisão por zero!")
    time.sleep(2)
    os.system("cls")

# Código principal
os.system("cls")  # Limpa antes de tudo começar
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

somar(n1, n2)
subtrair(n1, n2)
multiplicar(n1, n2)
dividir(n1, n2)

print("Operações finalizadas!")