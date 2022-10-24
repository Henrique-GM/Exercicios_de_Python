numero1 = int(input('Digite o intervalo inicial: '))
numero2 = int(input('Digite o intervalo final'))
print('\n')

while numero1 >= numero2:
    numero1 = int(input('Digite o primeiro intervalo menor que o segundo: '))
    numero2 = int(input('Digite o intervalo final: '))

for i in range(numero1, numero2 + 1):
    if i % 2 != 0:
        print(i, end=' ')
