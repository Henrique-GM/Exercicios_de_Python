lista = []


def sorteia():
    from random import randint

    for i in range(0, 5):
        lista.append(randint(0, 5))
    print('A lista criada foi:', lista)


def soma_par():
    soma = 0
    for i in lista:

        if i % 2 == 0:
            soma += i

    print('A soma dos números pares é:', soma)


sorteia()
soma_par()
