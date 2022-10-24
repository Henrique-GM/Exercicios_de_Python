auxiliar = 0
maior = 0
menor = 0

while True:
    numero = int(input('Digite um número: '))

    if numero < 0:
        break

    if auxiliar == 0:
        maior = numero
        menor = numero
        auxiliar += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print('\n')
print(f'O maior número é {maior} e menor {menor}')
