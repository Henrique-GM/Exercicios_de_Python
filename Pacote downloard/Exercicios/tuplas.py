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
