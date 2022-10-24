"""
--CONJUNTOS--

- Em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos da Matematica

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática

- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisarmos armazenar elementos
mas não precisamos nos importar com a ordenação deles. Quando não precisamos nos preocupar com chaves, valores e itens
duplicados.

Os conjuntos (sets) são referenciados em Python com chaves

Diferença entre conjuntos (set) e mapas (dicionários) em Python:
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7}) # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem
gerar erros e não fará parte do conjunto

# Forma 2 = mais comum

s1 = (1, 2, 3, 4, 5, 5)
print(s)
print(type(s))

# Podemos verificar se um determinado elementos está em um conjunto

if 3 in s1:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Lista aceitam valores duplicados, então teremos 7 elementos
lista = [10, 12, 13, 14, 15, 16, 16]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então teremos 7 elementos
tupla = 10, 12, 13, 14, 15, 16, 16
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionários NÃO aceitam valores duplicados, então teremos 6 elementos
dicionario = {}.fromkeys([10, 12, 13, 14, 15, 16, 16], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionarios)} elementos')

# conjuntos NÃO aceitam valores duplicados, então teremos 6 elementos
conjunto = {10, 12, 13, 14, 15, 16, 16}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como qualquer outro conjuntos Python podemos colocar tipos de dados misturados em Sets

"""