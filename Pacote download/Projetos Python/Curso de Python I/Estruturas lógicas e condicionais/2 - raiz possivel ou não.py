from math import sqrt

n1 = float(input('Digite um número: '))
print('\n')

if n1 < 0:
    print('Raiz impossível')
else:
    raiz = sqrt(n1)
    print(f'A raiz foi {raiz:.2f}')
