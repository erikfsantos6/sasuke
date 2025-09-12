import streamlit as st

st.title("Situação do Aluno")

# Entrada das 3 notas
nota1 = st.number_input("Nota 1")
nota2 = st.number_input("Nota 2")
nota3 = st.number_input("Nota 3")

# Botão para calcular
if st.button("Calcular"):
    media = (nota1 + nota2 + nota3) / 3
    st.write(f"Média: {media:.2f}")

    if media >= 7:
        st.write("Situação: Aprovado")
    elif media >= 4:
        st.write("Situação: Recuperação")
    else:
        st.write("Situação: Reprovado")
