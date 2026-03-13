from armazenamento import salvar_contas

def depositar(contas):
    numero = int(input('digite o número da conta: '))
    valor = float(input("Digite o valor do depósito: "))

    for conta in contas:
        if conta['numero'] == numero:
            conta['saldo'] += valor
            conta['extrato'].append (f'Depósito = +R${valor:.2f}')
            salvar_contas(contas)
            print('\nDepósito realizado com sucesso!')
            return
        
    print('\nConta não encontrada')

def sacar(contas):
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))

    for conta in contas:
        if conta['numero'] == numero:
    
            if conta['saldo'] >= valor:
                conta['saldo'] -=valor
                conta['extrato'].append (f'Saque: -R${valor:.2f}')
                salvar_contas(contas)
                print('Saque realizado com sucesso!')   

            else:
                print('Saldo insuficiente.')    
            return 

    print('Conta não encontrada.')  

def ver_saldo(contas):
    numero=int(input('Digite o número da sua conta: '))

    for conta in contas:
        if conta['numero'] == numero:
            print(f'Saldo da conta: R${conta["saldo"]:.2f}')
            return
        
    print('Conta não encontrada.')

def ver_extrato(contas):
    numero=int(input('Digite o número da conta: '))

    for conta in contas:
        if conta['numero'] == numero:
            
            print('===EXTRATO===')

            if not conta['extrato']:
                print('Nenhuma movimentação.')
                
            else:
                for movimento in conta['extrato']:
                    print(movimento)
            
            return
    print('Conta não encontrada.')