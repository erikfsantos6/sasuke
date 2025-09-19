import os
os.system("cls")

def main():
    menu = {
        1: {"dish":  "Itaipava", "price": 25.00},
        2: {"dish":  "picanha", "price": 20.00},
        3: {"dish":  "coca cola", "price": 18.00},
        4: {"dish":  "lasanha",  "price": 15.00},
        5: {"dish":  "pão com ovo", "price": 5.00},
    }

    total = 0.0

    while True:
        print("Menu:")
        for code, item in menu.items():
            print(f"{code}: {item['dish']} - R${item['price']}")

        choice = int(input("Escolha um prato pelo cadá pio(1-5): "))

        if choice in menu:
            total += menu[choice]["price"]
            print(f"Você escolheu: {menu[choice]['dish']}. Total até agora: R${total:.2f}")

        else:
            print("Código inválido. Tente novamente.")
            continue

        another = input("Você quer escolher outro prato? (sim/nao): ").lower()
        if another != "sim":
            break

    print(f"Total a ser pago: R${total:.2f}")

if __name__ == "__main__":
    main()
