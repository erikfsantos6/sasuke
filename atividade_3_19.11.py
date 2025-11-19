import csv

# ==========================
#   CLASSE USUÁRIO
# ==========================
class Usuario:
    def __init__(self, nome, data_nasc, rg, cpf):
        self.nome = nome
        self.data_nasc = data_nasc
        self.rg = rg
        self.cpf = cpf

    def to_list(self):
        """Retorna os dados no formato de lista (para salvar no CSV)."""
        return [self.nome, self.data_nasc, self.rg, self.cpf]


# ==========================
#   FUNÇÕES AUXILIARES
# ==========================
def input_validado(msg):
    """Garante que o usuário não deixe o campo vazio."""
    while True:
        valor = input(msg).strip()
        if valor:
            return valor
        print("⚠ O campo não pode ficar vazio! Tente novamente.")


# ==========================
#   CADASTRO
# ==========================
def cadastrar_usuarios(qtd=5):
    """Cadastra a quantidade de usuários especificada."""
    usuarios = []
    print("\n=== Cadastro de Usuários ===")

    for i in range(qtd):
        print(f"\n➡ Usuário {i+1}")

        nome = input_validado("Nome: ")
        data_nasc = input_validado("Data de Nascimento (dd/mm/aaaa): ")
        rg = input_validado("RG: ")
        cpf = input_validado("CPF: ")

        usuarios.append(Usuario(nome, data_nasc, rg, cpf))

    return usuarios


# ==========================
#   SALVAR NO CSV
# ==========================
def salvar_csv(usuarios, arquivo="Funcionarios.csv"):
    """Salva a lista de usuários no arquivo CSV."""
    with open(arquivo, "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)
        escritor.writerow(["Nome", "Data de Nascimento", "RG", "CPF"])

        for user in usuarios:
            escritor.writerow(user.to_list())

    print(f"\n✔ Arquivo '{arquivo}' salvo com sucesso!")


# ==========================
#   LER CSV
# ==========================
def ler_csv(arquivo="Funcionarios.csv"):
    """Lê e exibe os dados do arquivo CSV."""
    print("\n=== Conteúdo do Arquivo CSV ===\n")

    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            leitor = csv.reader(arq)

            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print("❌ O arquivo ainda não existe. Cadastre usuários primeiro.")


# ==========================
#   MENU PRINCIPAL
# ==========================
def menu():
    usuarios = cadastrar_usuarios()
    salvar_csv(usuarios)

    while True:
        print("\n=== MENU ===")
        print("1 - Ler Funcionarios.csv")
        print("2 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            ler_csv()
        elif opc == "2":
            print("\nEncerrando o programa...")
            break
        else:
            print("⚠ Opção inválida! Tente novamente.")


# ==========================
#   INICIAR PROGRAMA
# ==========================
menu()
