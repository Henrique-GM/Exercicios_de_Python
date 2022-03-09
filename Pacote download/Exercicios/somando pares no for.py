soma = 0
for i in range(1, 6 + 1):
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        soma += numero

print(soma)