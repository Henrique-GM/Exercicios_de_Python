def fatorial(numero, mostra_passo=False):
    multiplicador = 1
    i = 1

    while numero >= i:
        multiplicador *= numero

        if mostra_passo:
            print(f'{numero}', end='')

            if numero > 1:
                print('x', end='')

            if numero == 1:
                print(' = ', end='')

        numero -= i

    else:
        return multiplicador


print(fatorial(5, mostra_passo=True))
