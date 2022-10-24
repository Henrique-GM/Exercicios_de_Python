"""
Dicionários em python são representados por chaves

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Interar sobre dicionários

#
for chave in receita:
    print(chave)

# Mostrando só as chaves

for chave in receita:
    print(receita[chave])

# Deixando de forma melhor apresentável

for chave in receita:
    print(f' em {chave} recebi {receita[chave]}')

# Acessando as chaves

print(receita.keys())

# Encontrando os valores para no for usando '.keys'
# É uma forma Pythonica

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

# Acessando valores no for usando '.values'
# É uma forma Pythonica

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

# Gera um dicionário de itens. Lista contendo tuplas das chaves e valores

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# somando os valores, o seu máximo, mínimo e quantidade

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""