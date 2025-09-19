import os
os.system("cls")

def main():
    soma = 0
    contador =0

    while True:
        resposta = input("deseja colocar uma nota? (Sim ou Não):").strip().upper()

        if resposta == 'N':
            break
        nota = float(input("Digite a nota:"))
        soma += nota
        contador += 1

    if contador > 0:
        media = soma / contador
        print(f"\nVoçê inseriu {contador}notas.")
        print(f"A média das notas foi inseridas.")

    else:
        print("Nenhuma nota foi inserida.")

if __name__ =="__main__":
    main()            