produtos = ('fogão', 1500, 'TV', 1000, 'cama', 850)

print('-' * 26)
print('    LISTAGEM DE PREÇOS')
print('-' * 26)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<15}', end='')

    else:
        print(f'R$ {produtos[i]:.2f}')

print('-' * 26)
