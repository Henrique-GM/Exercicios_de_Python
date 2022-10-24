soma = 0

numero = int(input('Digite um número: '))
print('\n')

for i in range(1, numero + 1):
    cont = 0

    for j in range(1, i + 1):
        if i % j == 0:
            cont += 1

    if cont <= 2:
        soma += i

print(f'A soma dos primos foi: {soma}')
