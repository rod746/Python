#OPERACÕES BANCARIAS
#CRIAR UM SISTEMA BANCÁRIO  COM AS OPÇÕES: SACAR, DEPOSITAR E VISUALIZAR EXTRATO

deposito_final = 0
deposito = 0
saque_cliente = 0
saque_total = 0
extrato = []
limite = 500
print("    =Criando um Sistema  Bancário com Python=")
menu = ('''
    -=-=-=-==-=-=-=-=-=MENU-=-==-=-=-=-=-=--=-
    |  |   [1] -> SAQUE     [2] -> DEPÓSITO  |
    |  |   [3] -> EXTRATO   [4] -> SAIR      |
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-
''')
while True:
    print(menu)
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:      #SAQUE
        saque_cliente = float(input('Qual valor deseja realizar saque?: '))
        if saque_cliente < limite and saque_cliente < deposito_final:
            print(f'Você realizou um saque de R${saque_cliente:.2f}.')
            saque_total += saque_cliente 
            extrato.append('-R$ ')
            extrato.append(saque_cliente)
            saque_cliente = deposito_final - saque_cliente
        elif saque_cliente > limite:
            print(f'O valor de saque é maior do que o limite de {limite:.2f}.')
        else:
            print(f'Você não tem saldo suficiente.')
    elif opcao == 2:        #DEPOSITO
        deposito = float(input('Qual valor deseja depositar: '))
        if deposito > 0 and deposito < 1000:
            print(f'Deposito de R$ {deposito:.2f} realizado com sucesso.')
            deposito_final = deposito + deposito_final
            extrato.append('+ R$ ')
            extrato.append(deposito)
        else:
            print('Modo invalido ou valor excede máximo de deposito.')
    elif opcao == 3:        #EXTRATO
        extrato
        print(extrato)
        saldo = deposito_final - saque_total
        print(f'Total de depositos foi de R$ {deposito_final:.2f}\nRetiradas {saque_total:.2f}\nSaldo final de R${saldo:.2f}.')
    elif opcao == 4:        #SAIR
        print('Volte sempre!')
        break
    else:
        print('Digite uma opção válida')