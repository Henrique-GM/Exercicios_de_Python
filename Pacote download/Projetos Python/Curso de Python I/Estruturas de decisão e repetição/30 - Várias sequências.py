soma = 0
subtrai = 0

numero1 = int(input('Digite um número: '))
for i in range(1, numero1 + 1):
    soma += i

print(soma)
soma = 0
print('\n')


numero2 = int(input('Digite um número: '))
for z in range(1, numero2 + 1):
    if z % 2 == 0:
        subtrai += z

    else:
        soma += z

resultado = soma - subtrai

print(f'O resultado da subtração dos números pares pelos impares é: {resultado}')
soma = 0
print('\n')


numero3 = int(input('Digite um número: '))
for y in range(1, numero3 + 1):
    if y % 2 != 0:
        soma += y

print(soma)
