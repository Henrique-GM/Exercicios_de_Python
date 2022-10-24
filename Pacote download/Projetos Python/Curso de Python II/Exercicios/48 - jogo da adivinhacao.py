from random import randint

contador = 0

numero_inteiro = randint(0, 10)

print('Foi escolhido aleatoriamente um número de 0 a 10.')
print('Tente adivinhar')

correto = False

while not correto:
    participante = int(input('Qual é a sua escolha? '))

    contador += 1

    if participante == numero_inteiro:
        correto = True

print('Você está correto com {} tentativa(as)'.format(contador))
