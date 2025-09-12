import streamlit as st

def solicitar_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
            return nota
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

# Solicita as duas notas usando o laço while
nota1 = solicitar_nota("Digite a primeira nota: ")
nota2 = solicitar_nota("Digite a segunda nota: ")

# Calcula a média aritmética
media = (nota1 + nota2) / 2

# Mostra o resultado
print(f"A média do aluno é: {media}")
