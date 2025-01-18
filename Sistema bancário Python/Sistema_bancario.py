tela_inicial = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
Limite_saques = 3

while True:

    opcao = input(tela_inicial)

    if opcao == '1':
        valor = float(input("Informe o Valor do Depósito:   "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
        else:
            print("Falha na Operação! O valor de depósito é inválido")       

    elif opcao == '2':
        valor = float(input("Informe o Valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques > Limite_saques

        if excedeu_saldo:
            print("Saldo Insuficiente")

        elif excedeu_saques:
            print("Número de Saques Excedido")

        elif excedeu_limite:
            print("O valor do Saque excede o Limite ")      

        elif valor > 0:
            saldo -= valor
            extrato += f' Saque : R$ {valor:.2f}\n'
            numero_saques += 1      

        else:
            print('O valor informado é inválido ')    

    elif opcao == '3':
        print('\n===================EXTRAT0==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Seu saldo é : R$ {saldo:.2f}')
        print('==============================================')

    elif opcao == '4':
        break         
    else:
        print('Operação Inválida. Selecione novamente a opção desejada:')