"""
-----LISTAS----

Listas de python funcional como vetores, matrizes (arrays) em outras linguagens, com
a diferença de serem dinâmicas e também de poderem colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

# Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar à lista e adicionando elementos.
# Qualquer tipo de dado: Não possui tipo de dado fixo. podemos colocar qualquer tipo de dado

# As listas em python são representadas por colchete[]
# lista são mutáveis

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

lista2 = ['H', 'E', 'N', 'R', 'I', 'Q', 'U', 'E']

lista3 = []

lista4 = list(range(11))

# Vai ter espaçamento. Mesma coisa da lista2
lista5 = list('Henrique')

lista6 = [1, 6, 3 ,2, 5, 4]

# Percorrendo a lista para achar o número 1
if 1 in lista4:
    print('Encontrei o número 1')
else:
    print('Não foi encontrado')


# Podemos ordenar uma lista
print(lista6.sort())

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Para adicionar elementos em listas, utilizamos a função append
lista1.append(9)
print(lista1)

OBS: Com append, nós podemos adicionar um elemento por vez

lista1.append(10, 11, 12) # Vai dar um erro

# Uma lista dentro de outra lista. Elemento único
lista1.append([8, 3, 1])
print(lista1)

if [] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')


# Em vez de adicionar uma lista inteira(um elemento único), eles serão adicionados individualmente
(não aceita valor único)
lista1.extend(10, 11, 12)

# O append e extend adiciona elementos no final da lista

# Podemos inserir um novo elemento na lista informando a posição do índice
# Não substitui o valor inicial. Será deslocado para à direita
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos juntar duas listas

lista7 = lista1 + lista2
print(lista7)

# OU

lista1 = lista1 + lista2
print(lista1)

# Invertendo as listas
lista1.reverse()
lista2.reverse()

# OU

print(lista1[::-1])
print(lista2[::-1])

# Podemos copiar uma lista
lista1 = lista6.copy()
print(lista6)

# Para saber quantos elementos existem em uma lista
print(len(lista2))

# Podemos remover o último elemento de uma lista
print(lista6)
lista6.pop()
print(lista6)

# Podemos remover um elemento pelo índice
# OS elementos a direita desse índice serão deslocados para à esquerda
# Se não houver o índice dará um erro
lista2.pop(2)
print(lista2)

# Pode-se remover todos os elementos de uma lista
print(lista5)
lista5.clear()
print(lista5)

# Repetindo elementos da lista
lista1 = lista1 * 3

# Podemos converter uma string para uma lista
# Separa por espaço
exemplo = 'Curso de Python'
exemplo = exemplo.split()
print(curso)

# Podemos declarar que em vez de espaços para fazer o split. Podemos usar vírgula
exemplo2 = 'Curso,de,Python
exemplo2 = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista8 = ['Curso', 'De', Python]
# Pega a lista8, coloca espaça entre cada elemento e transforma em string
curso = ' '.join(lista6)
print(curso)

curso = '@'.join(lista8)
print(curso)

# Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista9 = [1, 2.56, True, False, 'Henrique' , 'h',[56, 85, 77], 1234]

# Iterando sobre listas usando for
for elemento in lista1:
    print(elemento)

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(somo)

# Iterando sobre listas usando While
carrinho = []
produto = ''

while produto != 'sair'
    print("Adicione um produto na lista ou digite 'sair' para sair")

    # recebendo o input do usuário
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'azul', 'amarelo', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

print(cores[-1]) # branco
print(cores[-2]) # amarelo
print(cores[-3]) #azul

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
# Mostrar chave e valor
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lsita9 = []
lista9.append(42)
lista9.append(42)
lista9.append(42)
lista9.append(42)

print(lista9)

# Encontrar o índice de um elemento na lista
numeros2 = [5, 6, 7, 8, 5,  9, 10]

print(numeros2.index(6))
print(numeros2.index(9))

# OBS: Caso não tenha esse elemento na lista, retorna erro

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros2.index(5))

# Podemos fazer uma buca dentro de um range, ou seja, qual índice começa a buscar
print(numeros2.index(5, 1)) # buscando a partir do índice 1

# Buscar o índice do valor 8, entre os índices 3 a 6
print(numeros2.index(8, 3, 6))

# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slicing de lista com o parâmetro 'início'

# lista10 = [1, 2, 3, 4]

print(lista10[1:]) # Iniciando no índice 1 pegando os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista10[:2]) # começa do 0 e pega até o índice 2
print(lista10[1:3]) # começa em 1, pega até o índice 3

# print(lista10[1::2]) # Começa em 1, vai até o final de 2 em 2
# print(lista10[::2]) # Começa em 0, vai até o final, de 2 em 2


# Invertendo valores em uma lista
nomes2 = ['Henrique', 'Gonçalves']

nomes2[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes2.reverse()
print(nomes2)

# soma, procurar valor máximo, minimo e tamanho de uma lista
# se os valores forem todos inteiros ou reais.

lista11 = [1, 2, 3, 4, 5, 6, 7]
print(sum(lista11)) # soma
print(max(lista11)) # máximo valor
print(min(lista11)) # mínimo valor
print(len(lista11)) # tamanho da lista

# Transforma lista em tupla
print(lista11)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista12 = [1, 2, 3]

num1, num2, num3 = lista12
print(num1)
print(num1)
print(num1)

OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# FORMA 1 - Deep Copy

lista13 = [1, 2, 3]
print(lista13)

nova = lista13.copy() # Cópia que não ocorre modificações na lista. Só na cópia

print(nova)

nova.append(4)

print(lista13)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta à outra. Isso
# em Python e chamado de Deep Copy (cópia profunda)

FORMA 2 - Shallow Copy

lista14 = [1, 2, 3]
print(lista14)

nova2 = lista # copia que também ocorre modificações na lista

print(lista14)
print(nova2)

# Houve cópia da lista, mas às modificações que deveria só ocorrer na cópia
# ocorre também na lista (Shallow Copy)

numero = [2, 5, 9, 1]
numero[2] = 3
# não irá funcionar
# numero[4] = 7

# Você adiciona um valor a listagem dessa maneira
numero.append(7)

# Organizando de maneira do menor para o maior
numero.sort()
print(numero)

# Organizando de forma reversa
numero.sort(reverse=True)
print(numero)

# Retorna a quantidade de elementos
print(f'Essa lista possui {len(numero)} elementos')

# Adicionando valores nas posições desejadas
numero.insert(2, 2)
print(numero)

# Removendo a primeira ocorrência da aparição do número. Mão indica o índice, mas o valor a ser removido
numero.remove(2)

# Se achar remove, se não, 'não encontrei o valor'
if 4 in numero:
    numero.remove(4)
else:
    print('Não encontrei o valor\n')

# inserindo valores na lista usando range
Exemplo = list(range(4, 11))
print(Exemplo)

# Outras formas de inserir valores na lista
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for i, valor in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {valor}')

print('\n')

# numericos = []
# for i in range(0, 5):
#   numericos.append(int(input('Digite um valor: ')))

# A partir do momento em que se iguala a lista na outra, o python cria uma ligação entre elas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\n')

# Para se criar uma cópia, e evitar ligação, utiliza-se[:]
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

"""
