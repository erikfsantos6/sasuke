# Criando uma lista para armazenar as notas
lista_notas = []

# Lendo as 3 notas do usuário e adicionando na lista
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

# Calculando a média das notas
media = sum(lista_notas) / len(lista_notas)

# Mostrando as notas informadas
for i, nota in enumerate(lista_notas, start=1):
    print(f"Nota {i}: {nota}")

# Informando a média
print(f"Média: {media:.2f}")
