impares = 0
soma = 0

for i in range(1, 99 + 1):
    if i % 2 != 0:
        impares = i

    soma += (impares / i)

print(f'O resultado da divisão e soma de impares e números inteiros é: {soma:.2f}')
