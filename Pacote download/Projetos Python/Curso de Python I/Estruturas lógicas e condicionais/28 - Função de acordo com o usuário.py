from math import pow
print('\n')
print('Digite "1" para à função geométrica\n'
      'Digite "2" para à função Ponderada\n'
      'Digite "3" para à função harmônica\n'
      'Digite "4" para à função aritmética\n')
print('\n')

x = float(input('Digite o valor de "x": '))
y = float(input('Digite o valor de "y": '))
z = float(input('Digite o valor de "z": '))

geometrica = pow(x * y * z, 1/3)
ponderada = (x + 2 * y + 3 * z) / 6
harmonica = 1 / (1 / x) + (1 / y) + (1 / z)
aritmetica = (x + y + z) / 3
print('\n')

escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print(f'{geometrica:.2f}')
elif escolha == 2:
    print(f'{ponderada:.2f}')
elif escolha == 3:
    print(f'{harmonica:.2f}')
elif escolha == 4:
    print(f'{aritmetica:.2f}')
