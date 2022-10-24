soma = 0

while True:
    numero = int(input('Digite um número: '))

    if numero >= 1000:
        break

    for i in range(1, numero + 1):

        if i % 3 == 0 or i % 5 == 0:
            soma += i

print(f' A soma dos múltiplos de 3 e 5 é: {soma}')
