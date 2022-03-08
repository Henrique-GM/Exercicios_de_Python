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


def leiaFloat(numero2):
    while True:
        try:
            numero = float(input(numero2))

        except(ValueError, TypeError):
            print('ERRO! por favor digite o número inteiro válido')

        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            break

        else:
            return numero


numero1 = leiaInt('Digite um valor inteiro: ')
numero2 = leiaFloat('Digite um valor float: ')

print(f'O valor inteiro digitado foi {numero1} e o real foi {numero2}')
