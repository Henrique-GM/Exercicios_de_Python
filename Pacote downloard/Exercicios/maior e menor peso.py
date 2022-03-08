maior = 0
menor = 0
aux = 0

for i in range(1, 5 + 1):
    peso = float(input('Digite seu peso: '))

    if aux == 0:
        maior = peso
        menor = peso
        aux += 1

    elif peso > maior:
        maior = peso

    elif peso < menor:
        menor = peso

print('O maior peso é: {:.2f}Kg'.format(maior))
print('O menor peso é: {:.2f}Kg'.format(menor))