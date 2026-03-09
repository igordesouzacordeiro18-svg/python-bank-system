from menu import menu
from contas import criar_conta,listar
from operacoes import depositar,sacar,ver_saldo,ver_extrato
def main():
    contas = []

    while True:
        menu()
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            criar_conta(contas)

        elif opcao == '2':
            listar(contas)
        
        elif opcao == '3':
            depositar(contas)

        elif opcao =='4':
            sacar(contas)

        elif opcao == '5':
            ver_saldo(contas)
        
        elif opcao == '6':
            ver_extrato(contas)

        elif opcao == '7':
            print('Saindo do programa')
            break

        else:
            print('Opção inválida')


main()