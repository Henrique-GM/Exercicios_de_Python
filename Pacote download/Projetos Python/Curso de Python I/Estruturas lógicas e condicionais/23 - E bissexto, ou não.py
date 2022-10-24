ano = int(input('Digite o ano: '))
print('\n')

if ano % 400 == 0 or ano % 4 == 0:
    if ano % 100 != 0:
        print('É um ano bissexto')

    else:
        print('Não é um ano bissexto')
else:
    print('Não é um ano bissexto')
