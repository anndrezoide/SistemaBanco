print("-=" * 18)
print("       GOLIATH NATIONAL BANK")
print("-=" * 18)

tupla = ('Andre Gomes', 'Itau', '00032-3', '5544', 'João Pedro', 'Bradesco', '00033-4', '3434', '234.456.789-10',
         '987.765.543-21')
conta = '12345-6'
agencia = '0056'
nome = 'André Gomes'
saldo = 0
tentativa = 3
rodada = 1
opcao = 0
while rodada <= tentativa:
    print("Tentativa {} de {}".format(rodada, tentativa))
    chute = input("Digite o numero da sua conta: ")
    chute2 = input("Digite o numero da sua agência: ")

    acertou = chute == conta
    acertou2 = chute2 == agencia

    if (acertou) and (acertou2):
        print("\nBem vindo, {}!".format(nome))
        while opcao != 4:
            print('\n')
            print('        MENU')
            print('=-' * 10)
            print('    1. EXTRATO\n    2. DEPOSITO\n    3. SAQUE\n    4. TRANSFERÊNCIAS\n    5. SAIR')
            print('=-' * 10)
            opcao = input('Digite uma das Opções: ')
            if opcao == "1":
                print('\nSaldo Disponivel: R$ {:.2f}'.format(saldo))
            elif opcao == "2":
                print('\nSaldo: R$ {:.2f}'.format(saldo))
                valor = float(input('Digite o valor a depositar: '))
                saldo = saldo + valor
                print('Saldo atual: R$ {:.2f}'.format(saldo))
            elif opcao == "3":
                print('\nSaldo: {:.2f}'.format(saldo))
                saque = float(input('Digite o valor do saque: '))
                saldo = saldo - saque
                if saldo < 0:
                    print('\nValor indisponivel para saque!: ')
                else:
                    print('Saldo atual: R$ {:.2f}'.format(saldo))
            elif opcao == '4':
                print('\nSaldo: R$ {:.2f}'.format(saldo))
                print('\n')
                nome = input('PARA QUEM TRANSFERIR \nDigite o nome completo: ')
                if nome in tupla:
                    banco = input('Banco: ')
                    if banco in tupla:
                        conta1 = input('Conta: ')
                        if conta1 in tupla:
                            agencia1 = input('Agência: ')
                            if agencia1 in tupla:
                                cpf = input('CPF: ')
                                if cpf in tupla:
                                    transf = float(input('Digite o valor da transferência: '))
                                    if saldo >= transf:
                                        saldo = saldo - transf
                                        print('\n***Transação realizada com sucesso!***')
                                        print('\nSaldo atual: R$ {:.2f}'.format(saldo))
                                    else:
                                        print('\n***Você não tem saldo suficiente para realizar esta transação!***')
                                else:
                                    print('CPF Inexistente...')
                            else:
                                print('Agência Inexistente...')
                        else:
                            print('Conta Inexistente...')
                    else:
                        print('Banco Inexistente...')
                else:
                    print('Nome inexistente!')
            elif opcao == '5':
                print('Goliath National Bank agradece. Volte sempre!')
                sys.exit("Fim")
                break
    else:
        print("Conta ou agencia incorretas. Tente novamente!")
    rodada = rodada + 1
print('***CONTA BLOQUADA***')