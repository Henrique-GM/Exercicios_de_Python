soma = 0
for i in range(0, 10):
    numero = float(input('Digite um número: '))

    if numero < 0:
        numero = 0

    soma += numero

media = soma / 10
print(f'A média foi: {media:.2f}')
