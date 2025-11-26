import os 
os.system("cls ||clear") 

#CRUD usando lista 
#CREATE=criar / salvar
#Read=buscar/selecionar
#Update=atualizar/modificar
#Delete=excluir 

#criando uma lista 
lista_cliente=[] 


#Create
# Lista de clientes
lista_cliente = []

# CREATE
print("=== CREATE - Adicionar / Inserir ===")
nome = input("Digite o nome do cliente para adicionar: ").strip()
lista_cliente.append(nome)
print(f"O nome '{nome}' foi inserido com sucesso!")

# READ
print("\n=== READ - Ler / Mostrar ===")
print("Lista atual de clientes:")
print(lista_cliente)

# UPDATE
print("\n=== UPDATE - Atualizar / Alterar ===")
nome_pra_atualizar = input("Digite o nome que deseja atualizar: ").strip()

# Comparação ignorando maiúsculas/minúsculas
# Procurar o nome real na lista
nome_encontrado = None
for item in lista_cliente:
    if item.lower() == nome_pra_atualizar.lower():
        nome_encontrado = item
        break

if nome_encontrado:
    novo_nome = input("Digite o novo nome: ").strip()
    indice = lista_cliente.index(nome_encontrado)
    lista_cliente[indice] = novo_nome
    print(f"O nome '{nome_encontrado}' foi atualizado para '{novo_nome}'.")
else:
    print(f"O nome '{nome_pra_atualizar}' não foi encontrado.")

print("\nLista atualizada:")
print(lista_cliente)

# DELETE
print("\n=== DELETE - Remover ===")
nome_pra_remover = input("Digite o nome que deseja remover: ").strip()

nome_encontrado = None
for item in lista_cliente:
    if item.lower() == nome_pra_remover.lower():
        nome_encontrado = item
        break

if nome_encontrado:
    lista_cliente.remove(nome_encontrado)
    print(f"O nome '{nome_encontrado}' foi removido com sucesso.")
else:
    print(f"O nome '{nome_pra_remover}' não foi encontrado.")

print("\nLista final:")
print(lista_cliente)
