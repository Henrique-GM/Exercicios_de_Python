from random import randint

print('RESOLVA OS PROBLEMAS DE MATEMÁTICA')
print('\n')

p1 = randint(1, 100)
p2 = randint(1, 100)
p3 = randint(1, 100)
p4 = randint(1, 100)
p5 = randint(1, 100)
p6 = randint(1, 100)
p7 = randint(1, 100)
p8 = randint(1, 100)
p9 = randint(1, 100)
p10 = randint(1, 100)

resp1 = int(input(f'Quanto é {p1} + {p2}: '))
resp2 = int(input(f'Quanto é {p3} + {p4}: '))
resp3 = int(input(f'Quanto é {p5} + {p6}: '))
resp4 = int(input(f'Quanto é {p7} + {p8}: '))
resp5 = int(input(f'Quanto é {p9} + {p10}: '))

erros = 0
acertos = 0

if resp1 == p1 + p2:
    acertos += 1
else:
    erros += 1

if resp2 == p3 + p4:
    acertos += 1
else:
    erros += 1

if resp3 == p5 + p6:
    acertos += 1
else:
    erros += 1

if resp4 == p7 + p8:
    acertos += 1
else:
    erros += 1

if resp5 == p9 + p10:
    acertos += 1
else:
    erros += 1

print('\n')
print(f'Você errou {erros} e acertou {acertos}')
