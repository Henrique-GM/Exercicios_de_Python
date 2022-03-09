def leiaInt(numero1):
    while True:
        try:
            numero = int(input(numero1))

        except(ValueError, TypeError):
            print('ERRO! por favor digite o número inteiro válido')

        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            break

        else:
            # caso utilize um "While True" com "return" em uma função, não precisa usar "break".
            return numero


def mostraMenu():
    print('''
------------------------------
        MENU PRINCIPAL
------------------------------
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
------------------------------
    ''')


def menu(lista):
    print(mostraMenu())

    contador = 1
    for i in lista:
        print(f'{contador} - {i}')

        contador += 1

    print()

    opcao = leiaInt('Qual é a sua opção: ')
    return opcao
