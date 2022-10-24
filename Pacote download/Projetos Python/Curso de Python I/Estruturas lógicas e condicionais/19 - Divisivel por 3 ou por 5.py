numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print('Divisão simultânea proibida')

elif numero % 3 == 0 and numero % 5 != 0:
    print('Divisão existente, mas não simultânea')

elif numero % 3 != 0 and numero % 5 == 0:
    print('Divisão existente, mas não simultânea')
