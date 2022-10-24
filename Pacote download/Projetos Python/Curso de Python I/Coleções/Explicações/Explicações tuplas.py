"""
----TUPLA----

Tuplas são bastante importante com listas.

Existem basicamente duas diferenças básicas

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

# Também é considerado um tupla dessa maneira
tuplas2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# cuidado: tupla com 1 elemento
tupla3 = (4) # Isso não é uma tupla

print(type(tupla3))

# Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses
tupla4 = (4,) # Isso é uma tupla
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

(4) - Não é tupla
(4,) - É tupla
4, - É tupla

# Podemos gerar uma tupla dinamicamente com range(inicia,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla6 = ('Henrique', 'Gonçalves', 'Mendes')

nome1, nome2, nome3 = tupla

print(nome1)
print(nome2)
print(nome3)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para

# Métodos para adição e remoção de elemento em tuplas não existem, pois são imutáveis

tupla7 = (1, 2, 3, 4, 5, 6)

print(sum(tupla7))
print(max(tupla7))
print(min(tupla7))
print(len(tupla7))

# Concatenação de tuplas
tupla8 = (1, 2, 3)
print(tupla8)

tupla9 = (4, 5, 6)
print(tupla9)

print(tupla8 + tupla9) # tuplas são imutáveis

print(tupla8)
print(tupla9)

tupla10 = tupla8 + tupla9

tupla9 = tupla7 + tupla8 # tuplas podem ser sobrescritos. A tupla não é uma constante

# verificar se um determinado elemento está contido na tupla
tupla11 = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla12 = (1, 2, 3)

for i in tupla12:
    print(i)

for indice, valor in enumerate(tupla12):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla13 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla13.count('b'))

aluno = tupla14('henrique')
print(aluno)

print(aluno.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.

# Exemplo 1

meses = ('J', 'F', 'M', 'A', 'M', 'JU', 'JUL', 'AGO', 'S', 'O', 'N', 'D')

# o acesso a elementos de uma tupla também é semelhante a de uma lista

# iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# OBS: Casa o elemento não exista, será gerado ValeuError
print(meses.index('exemplo'))

# Slicing

# Tupla[inicio:fim:paso]
print(meses[0:])
print(meses[5:])
print(meses[5:9])

# Por quê utilizar tuplas

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro. Isso porque trabalhar com elementos imutaveis
# traz segurança para o código

# Copiando uma tupla para outra
tupla15 = (1, 2, 3)
print(tupla15)

nova = tupla15 # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(tupla)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-2:])
print(lanche[-3:])
print(lanche)

# 1º jeito com for
print('\n')
for i in lanche:
    print(f'O {i} é delicioso')
print('Todos muito bons!')

print('\n')
print(len(lanche))

# 2º jeito com for
print('\n')
for i in range(0, len(lanche)):
    print(lanche[i])

# Tuplas são imutáveis
# lanche[1] = 'refrigerante'
# print(lanche[1])

# 3º jeito com for indicando posições
print('\n')
for i in range(0, len(lanche)):
    print(lanche[i] + f' na posição {i}')

# 4º jeito com for indicando posições
print('\n')
for proximo, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posição {proximo}')

# Vai printar em ordem
print('\n')
print(sorted(lanche))

# Tuplas com números
print('\n')
a = (2, 3, 4)
b = (5, 6, 7, 8, 5)

# concatena
c = a + b
print(c)

# quantidade
print(len(c))

# Quantas vezes aparece
print(c.count(2))

# mostra o index
print(c.index(5))

print('\n')

# mostra index atravez de deslocamento
print(c.index(5, 4))

# Pode ser inserido dados de tipos diferentes
pessoa = ('Henrique', 22, 'M', 83, 50)
# Apagando variáveis ou tuplas
# del(pessoa)

print(pessoa)

"""