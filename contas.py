from armazenamento import salvar_contas

def criar_conta(contas):
    nome = input('Digite seu nome completo: ')
    cpf = input('Digite seu CPF: ')
    numero = len(contas) + 1

    conta = {
        'nome': nome,
        'cpf': cpf,
        'numero': numero,
        'saldo': 0,
        'extrato': []
    }

    contas.append(conta)
    salvar_contas(contas)

    print('\nCadastro criado com sucesso!')
    print(f'Seu número de conta é: {numero}')
    input("Pressione Enter para continuar...")


def listar(contas):
    if not contas:
        print('Nenhuma conta foi criada.')
        input('Digite ENTER para voltar...')
        return

    for conta in contas:
        print(f'\nConta: {conta["numero"]}')
        print(f'Nome: {conta["nome"]}')
        print(f'CPF: {conta["cpf"]}')
        print(f'Saldo: {conta["saldo"]}')
    input('\nPressione ENTER para continuar...')
