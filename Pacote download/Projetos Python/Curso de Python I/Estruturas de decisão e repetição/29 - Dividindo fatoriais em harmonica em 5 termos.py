from math import factorial

soma = 0

for quantidade_termos in range(0, 4):
    numero = int(input('Digite um número: '))

    print('\n')

    for i in range(1, numero + 1):
        soma += (i / ((i * 2) / factorial(i)))

        print(f'A soma do {i}º termo é {soma}')

        if i == numero:
            print('\n')
            soma = 0
