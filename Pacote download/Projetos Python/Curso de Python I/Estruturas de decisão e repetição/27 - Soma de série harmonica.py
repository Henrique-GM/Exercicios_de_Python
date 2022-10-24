soma = 1

numero = int(input('Digite um número: '))
print('\n')

for i in range(1, numero + 1):
    soma += (1 / i)

print(f'{soma:.2f}')
