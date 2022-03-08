from math import sqrt, ceil, floor, trunc

# raiz do número
numero = float(input('Digite um número: '))
raiz = sqrt(numero)
print('A raiz {:.2f} é igual a {:.2f}\n'.format(numero, raiz))

# Arredondando para cima
numero2 = float(input('Digite um número: '))
raiz2 = sqrt(numero2)
print('A raiz {:.2f} é igual a {}\n'.format(numero2, ceil(raiz2)))

# Arredondando para baixo
numero3 = float(input('Digite um número: '))
raiz3 = sqrt(numero3)
print('A raiz {:.2f} é igual a {}\n'.format(numero3, floor(raiz3)))

# Truncando um número
numero4 = float(input('Digite um número: '))
raiz4 = trunc(numero4)
print(f'O número truncado é: {raiz4}')
