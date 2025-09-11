import streamlit as st
import time

# Título e cabeçalho
st.title("Atividade: 1")
st.header("Laço de repetição: For")


if st.button("Iniciar"):
    placeholder = st.empty()  
    for i in range(100, 121, 2):
        placeholder.info(i)
        time.sleep(1)
    st.header("Fim")
