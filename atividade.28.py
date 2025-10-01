# Criando a lista para armazenar as 4 notas
lista_notas = []

# Lendo as 4 notas do usuário
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

# Calculando a média das notas
media = sum(lista_notas) / len(lista_notas)

# Mostrando as notas
for i, nota in enumerate(lista_notas, start=1):
    print(f"Nota {i}: {nota}")

# Verificando a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Mostrando a média e a situação
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
