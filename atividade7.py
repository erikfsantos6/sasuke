import streamlit as st


st.title("Tabuada de Multiplicação")


numero = st.number_input("Digite um número para ver a tabuada:", step=2)


if numero != 0:
    st.write(f"### Tabuada do {numero}")
    for i in range(1, 11):
        resultado = numero * i
        st.write(f"{numero} x {i} = {resultado}")
else:
    st.warning("Digite um número diferente de zero para ver a tabuada.")
