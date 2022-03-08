from random import shuffle

aluno1 = str(input('Digite o aluno 1: '))
aluno2 = str(input('Digite o aluno 2: '))
aluno3 = str(input('Digite o aluno 3: '))
aluno4 = str(input('Digite o aluno 4: '))

# Criando um Array
lista = [aluno1, aluno2, aluno3, aluno4]

# Embaralhando a lista
shuffle(lista)

print('A ordem de precedencia será: ')
print(lista)


