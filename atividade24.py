import os
os.system("cls")

def main():
    soma = 0 
    Contador = 0


while True:
        numero = int(input("Digite um número positivo (ou um número negativo para parar): "))
        
        if numero < 0:
            break
        
        soma += numero
        contador += 1

if contador > 0:
        media = soma / contador
        print(f"\nVocê informou {contador} números.")
        print(f"A média aritmética é: {media:.2f}")
    
else:
        print("Nenhum número positivo foi informado.")

if __name__ == "__main__":
    main()
