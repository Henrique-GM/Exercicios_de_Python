menor = 0
maior = 0
auxiliar = 0

for i in range(0, 10):
    numero = float(input('Digite um número: '))

    if auxiliar == 0:
        maior = numero
        menor = numero
        auxiliar += 1

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')
