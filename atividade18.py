import streamlit as st

st.title("Laço de repetição")

st.write("Escreva um algoritmo que solicite duas notas para um aluno." \
"Caso seja menir que 0 ou maoir que 10, mostre a pergunta novamente." \
"Calcule e mosre a média arimética do aluno.")

nota1 = st.number_input("Digite a primeira nota:", min_value=0, max_value=10)
nota2 = st.number_input("Digite a segunda nota:", min_value=0, max_value=10)

while True:
    break

media = (nota1 + nota2) / 2

if st.button("Calcular média"):
    st.info(f"média: {media}")