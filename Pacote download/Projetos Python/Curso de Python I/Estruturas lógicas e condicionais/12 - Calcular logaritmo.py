from math import log

numero = int(input('Digite um número: '))
print('\n')

if numero <= 0:
    print('Número inválido')

elif numero == 1:
    print('Número inválido')

else:
    logaritmo = log(numero)
    print(f'O logaritmo do número foi: {logaritmo:.2f}')
