media = 0
soma = 0
while True:
    idade = int(input('Digite sua idade: '))

    if idade == 0:
        break

    soma += idade
    media += 1

print('\n')
print(f'A media de idades é {soma / media:.1f}')
