import streamlit as st

# Login e senha corretos (padrão para validação)
LOGIN_CORRETO = "erik freitas"
SENHA_CORRETA = "Gostoso445"


st.title("Validação de Login e Senha")


login = st.text_input("Digite seu login:")
senha = st.text_input("Digite sua senha:", type="password")


if login and senha:
    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        st.success("Login realizado com sucesso! ✅")
    else:
        st.error("Login ou senha incorretos. Tente novamente.")
