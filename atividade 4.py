import os
os.system("cls")

print("""
      
""")     


código = int (input("digite o código do prato desejado:"))

match código:
      case 1:
        print("pedido: picanha \ valor: R$25,00 reais ")
      case 2:
        print ("pedido:Lasanha \ valor: R$20,00 reais ")
      case 3:
        print ("pedido Stogooff \ valor: R$18,00 reais")
      case 4:
        print ("pedido: Bife Acebolado \ valor: R$15,00 reais")
      case 5:
        print("pedido pão com ovo \ valor: R$5,00 reais")
      case _:
        print("pedido não se encontra no cárdapio")





      
