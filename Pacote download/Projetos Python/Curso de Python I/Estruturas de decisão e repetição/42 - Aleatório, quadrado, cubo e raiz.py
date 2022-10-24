from random import randint
from math import sqrt

for i in range(0, 10):
    aleatorios = randint(1, 50)

    if i == 9:
        aleatorios = 0

    print(f'O quadrado {aleatorios ** 2} '
          f'o cubo {aleatorios ** 3} e a raiz '
          f'{sqrt(aleatorios):.2f}\n', end=' ')
