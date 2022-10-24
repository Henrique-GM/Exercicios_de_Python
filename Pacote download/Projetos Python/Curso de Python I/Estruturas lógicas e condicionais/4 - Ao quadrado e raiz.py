from math import sqrt

n1 = float(input('digite um número: '))
print('\n')

if n1 > 0:
    print(f'O número ao quadrado ficou: {n1 ** 2}')

    raiz = sqrt(n1)
    print(f'A raiz quadrada do número é {raiz:.2f}')
