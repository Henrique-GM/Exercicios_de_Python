from random import randint, choice

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

randomico_inteiro = randint(1, 4)

if (randomico_inteiro == 1):
    print('\nO aluno {} foi sorteado'.format(aluno1))

if (randomico_inteiro == 2):
    print('\nO aluno {} foi sorteado'.format(aluno2))

if (randomico_inteiro == 3):
    print('\nO aluno {} foi sorteado'.format(aluno3))

if (randomico_inteiro == 4):
    print('\nO aluno {} foi sorteado'.format(aluno4))

# usando autra função
n1 = str(input('\nDigite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))
