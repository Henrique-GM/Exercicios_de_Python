while True:
    numero = int(input('Digite um número: '))

    i = 0
    while i <= 10:
        print(f'{numero} x {i} = {numero * i}')
        i += 1

    resposta = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break