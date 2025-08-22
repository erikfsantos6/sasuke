import os
os.system("cls")
primera_nota = float (input("digite a primeira nota:"))
segunda_nota = float(input("digite a segunda nota"))

media = (primera_nota + segunda_nota) / 2

if media >= 7:
    resultado = "Aprovado"
else:
    print (" Reprovado")
