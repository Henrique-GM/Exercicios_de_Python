# PRIMEIRO JEITO DE FAZER
# informacoes_jogadores = {}
# lista_gols = []

# soma = 0

# for i in range(0, 1):
#    informacoes_jogadores['nome'] = str(input('Digite seu nome: '))
#    informacoes_jogadores['partidas'] = int(input('Digite quantas partidas jogou: '))

# for i in range(0, informacoes_jogadores['partidas']):
#    informacoes_jogadores['gols'] = int(input(f'Quantos gols você fez na {i} partida: '))

#    soma += informacoes_jogadores['gols']
#    informacoes_jogadores['soma'] = soma

#    lista_gols.append(informacoes_jogadores['gols'])
#    informacoes_jogadores['gols'] = lista_gols

# print('\n', informacoes_jogadores)

# print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# for chave, valor in informacoes_jogadores.items():
#    print(f'O campo {chave} tem o valor {valor}')

# print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# print(f'O jogador {informacoes_jogadores["nome"]} jogou {informacoes_jogadores["partidas"]} partidas')

# for i in range(0, informacoes_jogadores["partidas"]):
#    print(f'Na partida {i + 1} fez {lista_gols[i]}')
# print(f'foram {informacoes_jogadores["soma"]} feito pelo {informacoes_jogadores["nome"]}')

# SEGUNDO JEITO

time = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for i in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {i}: ')))

    # transformando dicionário em lista
    jogador['gols'] = partidas[:]

    # sum é uma função para somar
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resposta in 'SNsn':
            break

        print('Responda apenas [S/N].')

    if resposta in 'Nn':
        break

print('-=' * 30)
for i in jogador.keys():
    print(f'   {i:<15}', end='')
print()
print('-=' * 30)

for chave, valor in enumerate(time):
    print(f'{chave:>4}', end=' ')

    for i in valor.values():
        print(f'{str(i):<15}', end=' ')
    print()
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))

    if busca == '999':
        break

    if busca >= len(time):
        print(f'Não existe jogador vom o código {busca}!')

    else:
        print(f' -- LEVANTAMENTO DO JOGADOR{time[busca]["nome"]}: ')

        for i, gols in enumerate(time[busca]['gols']):
            print(f'No jogo{i+1} fez {gols} gols.')
    print('-=' * 40)
