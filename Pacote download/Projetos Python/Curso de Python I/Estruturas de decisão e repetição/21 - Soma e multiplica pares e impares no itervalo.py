numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print('\n')

if numero1 % 2 == 0 and numero2 % 2 == 0:
    for i in range(numero1, numero2 + 1):
        if i % 2 == 0:
            print(i, end=' ')

if numero1 % 2 != 0 and numero2 % 2 != 0:
    for i in range(numero1, numero2 + 1):
        if i % 2 != 0:
            print(i, end=' ')
