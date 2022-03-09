from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é sua jogada? '))

print('O computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))

if computador == 0:

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('O JOGADOR GANHOU')

    elif jogador == 2:
        print('O JOGADOR PERDEU')

    else:
        print('jogada invalida')

if computador == 1:

    if jogador == 0:
        print('O JOGADOR PERDEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('O JOGADOR GANHOU')

if computador == 2:

    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador == 1:
        print('JOGADOR PERDEU')

    elif jogador == 2:
        print('EMPATE')