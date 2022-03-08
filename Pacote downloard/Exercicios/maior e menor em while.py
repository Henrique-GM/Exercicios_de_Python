contador = 0
media = 0
maior = 0
menor = 0
soma = 0
resposta = ''
auxiliar = 0

while resposta != 'N':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    contador += 1

    if auxiliar == 0:
        maior = numero
        menor = numero
        auxiliar += 1

    elif numero > maior:
            maior = numero

    elif numero < menor:
            menor = numero

    resposta = str(input('voçê que continuar, "S" ou "N": ')).strip().upper()[0]

print('\n')
media = soma / contador

print('A média foi: {}'.format(media))
print('A soma foi: {}'.format(soma))
print('O maior {} e o menor {}'.format(maior, menor))