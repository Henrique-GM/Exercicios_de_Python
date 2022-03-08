from random import randint

lista = []
jogos = []

quantidade = int(input('Quantos jogos você quer sortear? '))
total = 1

while total <= quantidade:
    contador = 0

    while True:
        numero = randint(1, 60)

        if numero not in lista:
            lista.append(numero)

            contador += 1

        if contador >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, Lista in enumerate(jogos):
    print(f'jogo {i + 1}: {Lista}')
