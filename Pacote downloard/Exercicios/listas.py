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

# Removendo elementos na posição final
numero.pop()
print(numero)

# Removendo elementos na posição desejada
numero.pop(2)
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
