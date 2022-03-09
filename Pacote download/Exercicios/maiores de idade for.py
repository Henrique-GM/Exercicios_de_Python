from datetime import date

contador = 0
contador2 = 0

for i in range(1, 5 + 1):

    nome = str(input('Digite seu nome: ')).split()
    ano = int(input('Digite o ano de seu nascimento: '))

    ano_atual = date.today().year
    conferir = ano_atual - ano

    if conferir >= 18:
       contador += 1

    elif conferir < 18:
        contador2 += 1

print('\nMaiores de idade: {}'.format(contador))
print('Menores de idade: {}'.format(contador2))