altura = float(input('Digite à altura: '))
base_maior = float(input('Digite a base maior do trapézio: '))

if base_maior > 0:
    base_menor = float(input('Digite a base menor do trapézio: '))

    if base_menor > 0:
        print(f'A área do trapézio é {(base_maior + base_menor) * altura / 2:.2f}')

    else:
        print('Digite o valor da base menor maior que zero')

else:
    print('Digite o valor da base maior, maior que zero')
