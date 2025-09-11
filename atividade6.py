import streamlit as st

st.title("Tabuada de Multiplicação")

# Solicita o número do usuário
numero = st.number_input("Digite um número para ver a tabuada:", step=1, format="%d")

if numero:
    st.subheader(f"Tabuada do {int(numero)}:")
    for i in range(1, 11):
        resultado = int(numero) * i
        st.write(f"{int(numero)} x {i} = {resultado}")
