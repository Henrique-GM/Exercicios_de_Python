"""
----DICIONÁRIOS----

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por
mapas.

Dicionários são coleções de tipo chave/valor.

Dicionários são representados por chaves

print(type({}))

# OBS: Sobre dicionários
    - a separação entre chave e valor é feita por ':' 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - podemos misturar tipos de dados

# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises2)
print(type(paises2))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

#OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError
print(paises['ru'])

Forma 2 - Acessando via get - Recomendado
# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

print(paises.get('br'))
print(paises.get('ru'))

----None----

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

- Podemos utilizar None quando queremos criar uma variável e inicializá-la com
um tipo sem tipo, antes de querermos receber um valor final

# O Tipo None é um tipo sem tipo, conhecido também como um tipo vazio.
OBS: O tipo None em python é sempre considerado falso

if paises:
    print(f'Encontrei o pais {paises}')
else:
    print('Não encontrei o pais')

# definindo um valor padrão, caso não encontre.
# Podemos definir um valor padrão, caso não encontre o objeto com a chave informada
# Está falando o seguinte. Pega pra mim a chave 'py', caso não encontre
# coloque o valor 'Não encontrei o pais'

pais = paises.get('py', 'Não encontrei o pais')

print(f'Encontrei o pais {pais}')

----/----

# Conferindo se exite uma chave em um dicionário
print('br' in paises)
print('ru' in paises)

# Podemos utilizar qualquer tipo de dado inclusive (int, float, string boolean), inclusive lista, tupla
# dicionário, como chaves de dicionários

# É interessante utilizar tuplas em dicionários, pois nesse exemplo, garantimos que
as chaves são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tóquio'
    (40.7128, 74.0060): 'Escritório em Nova York'
    (37.7749, 22.4194): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais cumum

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.updade({'mai': 500})
print(recita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.updade({'mai': 600})
print(receita)

# CONCLUSÃO 1: A Forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÂO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita2 = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1

ret = receita2.pop('mar')
print(ret)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita2['fev']
print(receita2)

# OBS: Se a chave não existir, será gerada um KeyError
# OBS: Neste caso o valor removido não será retornado

# Importância dos dicionários

# imagine que tenha um comércio eletrônico, onde temos um carrinho de compras
# na qual adicionamos produtos.

# Produto 1, 2, 3, 4
    - nome
    - quantidade
    - preço

# 1 - Podemos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 5', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação do produto

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

carrinho2 = ()

produto3 = ('Playstation 5, 1, 2300.00')
protuto4 = ('God of War 4, 1, 150.00')

carrinho2 = (produto3, produto4)

print(carrinho2)

# Teríamos que saber qual é o índice de cada informação do produto

# 3 - Poderiamos utilizar um Dicionário para isso? Sim

carrinho3 = []

produto5 = {'Playstation 5, 1, 2300.00'}
protuto6 = {'God of War 4, 1, 150.00'}

carrinho3.append(produto5)
carrinho3.append(produto6)

print(carrinho3)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter
# certeza sobre cada informação.


# Métodos de dicionários

dici = dict(a=1, b=2, c=3)

print(dici)
print(type(d))

# Limpar o dicionário (Zerar dados)

dici.clear()
print(dici)

# Copiando um dicionário para outro

# Forma 1 Deep Copy

novo = dici.copy()
print(novo)

novo['dici'] = 4

print(dici)
print(novo)

# Forma 2 Shallow Copy

novo2 = dici
print(novo2)

novo['dici'] = 4

print(dici)
print(novo2)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

# Cada um desses elementos viraram uma chave. e o 'desconhecido virou o valor para cada um'
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# Pra cada caractere de teste (exeto caracteres repetidos, porque em python não possui chavees repetidas)
terá o valor 'valor'

veja = {}.fromkeys('teste', 'valor')
print(veja)

# Pode utilizar o range
veja = {}.fromkeys(range(0, 9), 'novo')
print(veja)
"""