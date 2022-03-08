valores = []
par = []
impar = []

for i in range(0, 5):
    valores.append(int(input('Digite um número: ')))

    if valores[i] % 2 == 0:
        par.append(valores[i])

    else:
        impar.append(valores[i])

print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')

valores = par + impar
print(f'todos os valores são {valores}')
