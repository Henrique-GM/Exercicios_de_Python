# declarando uma lista dentro da outra
numeros = [[], []]

for i in range(0, 7):
    valores = int(input('Digite um valor: '))

    if valores % 2 == 0:
        numeros[0].append(valores)

    else:
        numeros[1].append(valores)

numeros[0].sort()
numeros[1].sort()

print(f'Os números pares são {numeros[0]} e os impares {numeros[1]}')
