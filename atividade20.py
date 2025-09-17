# Dados corretos (definidos no sistema)
login_correto = "Bumbum quente"
senha_correta = "DE bruny"

# Loop até o usuário digitar corretamente
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("Login realizado com sucesso! ✅")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.\n")
