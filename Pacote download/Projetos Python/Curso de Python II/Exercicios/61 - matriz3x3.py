# evitando usar o .append. Subistituindo o 0 pelo valor digitado
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):

        matriz[i][j] = int(input(f'Digite um valor para[{i}][{j}]: '))

for i in range(0, 3):
    for j in range(0, 3):

        # 5 espaços e centralizado
        print(f'[{matriz[i][j]:^5}]', end='')

    # O end='' e o print, é para deixar em forma de matriz
    print()
