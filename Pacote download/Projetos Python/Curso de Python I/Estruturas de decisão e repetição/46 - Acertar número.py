from random import randint

numero_aleatorio = randint(1, 10)

while True:
    chute = int(input('Chute um número para acertar: '))

    if chute > numero_aleatorio:
        print('O chute que deu foi maior que o número')

    elif chute < numero_aleatorio:
        print('O chute que deu foi menor que o número')

    elif chute == numero_aleatorio:
        print('Acertou o número!')
        break

    print('\n')
