numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print('\n')

if numero1 > numero2:
    print(f'O numero maior é {numero1}')
elif numero2 > numero1:
    print(f'O numero maior é {numero2}')
else:
    print('Os números são repetidos')
