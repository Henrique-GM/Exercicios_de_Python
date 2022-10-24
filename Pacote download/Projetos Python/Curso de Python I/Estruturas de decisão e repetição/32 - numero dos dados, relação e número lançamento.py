from random import randint

dado1 = 0
dado2 = 0

lancamentos = randint(1, 9)

for i in range(1, lancamentos):

    for z in range(0, 4):
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)

    if dado1 > dado2:
        print(f'No {i}º lançamento o maior foi {dado1} e o menor {dado2}')

    elif dado2 > dado1:
        print(f'No {i}º lançamento o maior foi {dado2} e o menor {dado1}')

    else:
        print(f'No {i}º o {dado1} e {dado2} são iguais')
