cont = 0
soma = 0

print('DIGITE AS NOTAS ENTRE 10 E 20')
print('\n')

while True:
    notas = float(input('Digite sua nota: '))

    soma += notas
    cont += 1

    if notas < 10 or notas > 20:
        break

media = soma / cont

print(f'A média das notas foi {media:.2f}')
