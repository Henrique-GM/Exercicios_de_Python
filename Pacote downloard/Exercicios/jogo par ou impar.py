from random import randint

contador = 0
escolha = ''

while True:
    soma = 0

    computador = randint(0, 10)

    escolha = str(input('Escolha par ou impar[P/I]: ')).strip().upper()[0]

    while escolha not in 'PI':
        escolha = str(input('Escolha par ou impar[P/I]: ')).strip().upper()[0]

    if escolha == 'P':
        par = int(input('Digite o número par: '))

        soma += par + computador

        if soma % 2 == 0:
            print(f'O resultado foi {soma}')
            print('Você venceu!')

            contador += 1

        else:
            print('Você perdeu')
            break

    elif escolha == 'I':
        impar = int(input('Digite o número impar: '))

        soma += impar + computador

        if soma % 2 != 0:
            print(f'O resultado foi {soma}')
            print('Você venceu!')

            contador += 1

        else:
            print('Você perdeu')
            break

print(f'Você venceu {contador} vezes')
