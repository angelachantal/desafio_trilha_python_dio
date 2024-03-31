menu = """
Digite o número da operação desejada:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair

=======> """

saldo = 0
valor_max = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido. Informe um valor maior que 0!")

    elif opcao == "2":
        
        valor = float(input("Valor do saque: "))

        saldo_insuficiente = valor > saldo

        limite_valor = valor > valor_max

        limite_saque = numero_saques > LIMITE_SAQUES

        if saldo_insuficiente:
            print("Saldo insuficiente.")

        elif limite_valor:
            print("O valor de saque não pode exceder R$ 500,00.")

        elif limite_saque:
            print("O limite de saques diário já foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido")

    elif opcao == "3":
        if saldo == 0:
            print("\n================ EXTRATO ================ \nNão foram realizadas movimentações. \n==========================================")
        else:
            print(f"\n================ EXTRATO ================ \nSaldo: R$ {saldo:.2f} \n==========================================")
    
    elif opcao == "4":
        break

    else:
        print("Opção inválida.")