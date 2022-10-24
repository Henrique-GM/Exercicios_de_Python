from math import sqrt

n1 = float(input('Digite um número inteiro: '))
print('\n')

if n1 < 0:
    print(f'O Quadrado do numero {n1} foi {n1 ** 2}')
else:
    raiz = sqrt(n1)
    print(f'A raiz do número foi {raiz:.2f}')
