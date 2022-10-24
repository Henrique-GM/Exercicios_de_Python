numero = int(input('Digite um número: '))
print('\n')

for i in range(1, numero + 1):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print(i, end=' ')
