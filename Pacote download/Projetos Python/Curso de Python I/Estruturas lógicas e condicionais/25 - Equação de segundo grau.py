from math import sqrt

a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))
print('\n')

delta = b ** 2 - 4 * a * c

raiz_de_delta_I = (-1 * b + sqrt(delta)) / 2 * a
raiz_de_delta_II = (-1 * b - sqrt(delta)) / 2 * a

if delta < 0:
    print('Não existe solução real real')

elif a == 0:
    print('Não é equação de segundo grau')

elif delta == 0:
    print(f'A solução possui uma única solução real que é: {raiz_de_delta_I}')

elif delta > 0:
    print(f'Possui duas soluções reais que é: {raiz_de_delta_I:.2f} e {raiz_de_delta_II:.2f}')
