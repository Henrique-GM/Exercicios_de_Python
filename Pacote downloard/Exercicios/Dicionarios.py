# pra declarar é preciso usar aspas simples
pessoas = {'nome': 'Henrique', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])

print('\n')

# Já que está entre aspas simples, tem que utilizar aspas duplas
print(f'O {pessoas["nome"]} tem {"idade"} anos')

print('\n')

# Deletando informações no dicionário
# del pessoas['idade']

# dando print nas chaves
print(pessoas.keys())

print('\n')

# print nos itens
print(pessoas.items())

# Acessando chaves
for chave in pessoas.keys():
    print(chave)

print('\n')

# pega tanto as chaves como os itens inseridos nela
for chave in pessoas.items():
    print(chave)

print('\n')

# Pega todos os valores inseridos na chaves
for chave in pessoas.values():
    print(chave)

print('\n')

# Dando um print formatado em itens
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

print('\n')

# Deletando elemento
del pessoas['sexo']
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

print('\n')

# Modificando valores
pessoas['nome'] = 'Henrique Gonçalves Mendes'
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

print('\n')

# Adicionando novos valores
pessoas['peso'] = '84.5'
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

print('\n')

# Adicionando dicionario dentro de uma lista
brasil = []
estado1 = {'UF': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])

print(brasil[0]['UF'])
print(brasil[1]['sigla'])

print('\n')

# Adicionando dicionários dentro de uma lista usando for range
# Um outro jeito de por dicionário é o dict()
unidade_federativa = dict()
Brasil = list()

for i in range(0, 3):
    unidade_federativa['uf'] = str(input('Unidade Federativa: '))
    unidade_federativa['Sigla'] = str(input('Sigla de estado: '))
    # Copiando os dicionários para dentro da lista
    Brasil.append(unidade_federativa.copy())

print('\n')

# deixando mais apresentável
for estado in Brasil:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem o valor {valor}')

print('\n')

for estado in Brasil:
    print(estado)
