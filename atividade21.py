import streamlit as st

# Dados corretos (login e senha)
login_correto = "admin"
senha_correta = "1234"


if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 3


st.title("Login com Limite de Tentativas")


login = st.text_input("Digite seu login:")
senha = st.text_input("Digite sua senha:", type="password")


if st.session_state.tentativas > 0:
    if login and senha:
        if login == login_correto and senha == senha_correta:
            st.success("Login realizado com sucesso! ✅")
            st.session_state.tentativas = 3  
        else:
            st.error("Número de tentativas excedido. O programa será finalizado.")