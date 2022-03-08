from random import randint
from time import sleep

# função para ordenação de dicionários
from operator import itemgetter

ranking = []

# pode-se fazer um dicionário dessa forma
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)

# transforma dicionários em lista com tuplas
# Ordenado por chave '0'. Ordenado por valor '1'
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)

for i, valor in enumerate(ranking):
    print(f'{i + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)
