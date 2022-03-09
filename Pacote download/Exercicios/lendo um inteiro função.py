def leia_inteiro(numero):
    if numero.isnumeric():
        print(f'Você digitou {numero}')

    if numero.isdecimal:
        print(f'Você digitou {numero}')

    else:
        print('Não é um número')


numero = (input('Digite um número inteiro: ')).strip()

leia_inteiro(numero)
