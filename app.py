# Um conversor de Unidades

import time

value = 1.60934

while True:

    time.sleep(1)
    print("\n------------------------------")
    print("Digite 1 para converter KM/H para MPH")
    print("Digite 2 para converter MPH para KM/H")
    print("Digite 0 para sair")
    print("------------------------------")
    time.sleep(0.5)

    try:
        quest = int(input("Escolha uma opção:"))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número (0, 1 ou 2).")
        continue

    if quest == 0:
        print("Saindo...")
        time.sleep(0.5)
        print("Saindo..")
        time.sleep(0.5)
        print("Saindo.")
        time.sleep(1)
        break

    elif quest == 1:
        try:
            km = float(input("Digite o valor em KM/H:"))
            mph = km / value 
            print(f"MPH = {mph:.2f}")

        except ValueError:
            print("valor inválido, tente novamente")
            time.sleep(0.5)
            continue
    
    elif quest == 2:
        try:
            mph = float(input("Digite o valor em MPH:"))
            km = mph * value
            print(f"KM/H = {km:.2}")

        except ValueError:
            print("valor inválido, tente novamente")
            time.sleep(0.5)
            continue

    else:
        print("tente as opções 0, 1 ou 2")
        time.sleep(0.5)
        continue