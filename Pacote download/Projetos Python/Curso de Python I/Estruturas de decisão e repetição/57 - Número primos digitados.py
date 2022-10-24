numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
print('\n')

for i in range(numero1, numero2):
    cont = 0

    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1

    if cont <= 2:
        print(i)
