def linha():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(s)


# simbolo de desempacotamento '*'
def contador(*numeros):
    for i in numeros:
        tamanho = len(numeros)
        print(f'Recebi os valores {numeros} e a quantidade é {tamanho}')
        break


def dobra(lista):
    auxiliar = 0
    while auxiliar < len(lista):
        lista[auxiliar] *= 2

        auxiliar += 1


# docstring
def passos(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    i: início da contagem
    f: fim da contagem
    p: paso da contagem
    return: sem retorno
    """

    c = i

    while c <= f:
        print(f'{c}', end=' ')

        c += p

    print('fim!')


# Parâmetros opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


# Retornando valores
# Parâmetros opcionais
def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s


def par(n=0):
    if n % 2 == 0:
        return True

    else:
        return False


# Programa principal
linha()
print('  CURSO DE PYTHON  ')
linha()
print('  APRENDENDO PYTHON  ')
linha()
print('  HENRIQUE GONÇALVES MENDES  ')

print()

# Outra forma de usar função com parâmetro
titulo('  CURSO DE PYTHON  ')
titulo('  APRENDENDO PYTHON  ')
titulo('  HENRIQUE GONÇALVES MENDES  ')

# função para soma
soma(4, 5)
soma(8, 5)
soma(7, 8)

# pode ser feita de forma mais explicita
soma(a=8, b=9)

# pode-se mudar a ordem
soma(b=9, a=11)

print()

# EXEMPLO DE EMPACOTAMENTO(pode passar uma quantidade desconhecida de parâmetros)
contador(2, 1, 7)
contador(7, 9)
contador(4, 4, 9, 7, 3, 1)

print()

# funções também aceitam listas(não precisa desempacota-las, porque é uma variável composta)
valores = [4, 5, 9, 8, 3, 6]
dobra(valores)
print(valores)

# interactive help(). Ajuda no auxílio da documentação
# Help()
# Também da pra usar o nome da função(input.__doc__)

# docstrings
passos(2, 10, 2)
help(passos)

# Parâmetros opcionais
somar(2, 8, 9)
somar(5, 7)
somar()

# pode personalizar o retorno de variáveis
# Parâmetros opcionais
# Retornando valores
r1 = somar2(2, 8, 9)
r2 = somar2(5, 7)
r3 = somar2()

print(f'Os resultado foram {r1} {r2} {r3}')


num = int(input('Digite um número: '))
par(num)

if par(num):
    print('É par')

else:
    print('Não é par')
