matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
auxiliar = 0

for i in range(0, 3):
    for j in range(0, 3):

        matriz[i][j] = int(input(f'Digite o valor para[{i}][{j}]: '))

for i in range(0, 3):
    for j in range(0, 3):

        print(f'[{matriz[i][j]:^5}]', end='')

    print()

for i in range(0, 3):
    for j in range(0, 3):

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

        soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]

        if matriz[1][0] >= matriz[1][1] >= matriz[1][2]:

            maior_valor_segunda_linha = matriz[1][0]

        elif matriz[1][1] >= matriz[1][0] >= matriz[1][2]:

            maior_valor_segunda_linha = matriz[1][1]

        else:

            maior_valor_segunda_linha = matriz[1][2]

print(f'\nA soma de todos os valores pares são: {soma_pares}')
print(f'A soma de todos os valores da terceira coluna: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha foi: {maior_valor_segunda_linha}')

# Outro jeito de fazer

for i in range(0, 3):
    for j in range(0, 3):

        matriz[i][j] = int(input(f'Digite o valor para[{i}][{j}]: '))

for i in range(0, 3):
    for j in range(0, 3):

        print(f'[{matriz[i][j]:^5}]', end='')

    print()

for i in range(0, 3):
    for j in range(0, 3):

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

for i in range(0, 3):

    # A linha varia, más a coluna não.
    soma_terceira_coluna += matriz[i][2]

# A coluna varia, más a linha não
for j in range(0, 3):
    if auxiliar == 0:
        maior_valor_segunda_linha = matriz[1][j]
        auxiliar += 1

    elif matriz[1][j] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = matriz[1][j]
