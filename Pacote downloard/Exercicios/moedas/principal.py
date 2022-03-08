from utilidades import moeda
from utilidades import dado

preco = float(input('Digite um preço: '))

print()

print(f'Aumentando 10%, temos: {moeda.aumentar(preco, True)}')
print(f'Diminuindo 13%, temos: {moeda.reduzir(preco, True)}')
print(f'O dobro desse número foi: {moeda.dobro(preco, True)}')
print(f'Metade desse número foi: {moeda.metade(preco, True)}')

print()

preco = dado.leiaDinheiro('Digite um valor: ')

print()

moeda.resumo(preco, 20, 12)
