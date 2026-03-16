from armazenamento import salvar_contas

def depositar(contas):
    numero = int(input('digite o número da conta: '))
    valor = float(input("Digite o valor do depósito: ").replace("," , "."))

    for conta in contas:
        if conta['numero'] == numero:
            conta['saldo'] += valor
            conta['extrato'].append (f'Depósito = +R${valor:.2f}')
            salvar_contas(contas)
            print('\nDepósito realizado com sucesso!')
            input("Pressione Enter para continuar...")
            return
        
    print('\nConta não encontrada')
    input('Digite ENTER para voltar...')

def sacar(contas):
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: ").replace("," , "."))

    for conta in contas:
        if conta['numero'] == numero:
    
            if conta['saldo'] >= valor:
                conta['saldo'] -=valor
                conta['extrato'].append (f'Saque: -R${valor:.2f}')
                salvar_contas(contas)
                print('\nSaque realizado com sucesso!') 
                input("Pressione Enter para continuar...")  

            else:
                print('Saldo insuficiente.')
                input('Digite ENTER para voltar...')
    
            return 

    print('\nConta não encontrada.')
    input('Digite ENTER para voltar...')
  

def ver_saldo(contas):
    numero=int(input('Digite o número da sua conta: '))

    for conta in contas:
        if conta['numero'] == numero:
            print(f'Saldo da conta: R${conta["saldo"]:.2f}')
            input('\nDigite ENTER para voltar...')
            return
        
    print('\nConta não encontrada.')
    input('Digite ENTER para voltar...')


def ver_extrato(contas):
    numero=int(input('Digite o número da conta: '))

    for conta in contas:
        if conta['numero'] == numero:
            
            print('===EXTRATO===')

            if not conta['extrato']:
                print('Nenhuma movimentação.')
                input('Digite ENTER para voltar...')

                
            else:
                for movimento in conta['extrato']:
                    print(movimento)
                    
                input('\nDigite ENTER para voltar...')
            
            return
    print('\nConta não encontrada.')
    input('Digite ENTER para voltar...')
