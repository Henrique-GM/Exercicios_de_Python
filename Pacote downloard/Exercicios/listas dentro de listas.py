# criando uma lista
teste = list()
teste.append('Henrique')
teste.append(22)
print(teste)
print('\n')

# criando lista dentro de uma lista.Evitando também uma ligação usando[:]
informacoes = list()
informacoes.append(teste[:])
print(informacoes)
print('\n')

# mudando informações de teste.
teste[0] = 'Maria'
teste[1] = 20
informacoes.append(teste[:])
print(informacoes)
print('\n')

# outra forma de declarar.
exemplo = [['João', '19'], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(exemplo)
print(exemplo[0][0])
print(exemplo[2][1])
print('\n')

# printando exemplo com for
for i in exemplo:
    print(i)
print('\n')

# printando exemplo com for, só os nomes
for i in exemplo:
    print(i[0])
print('\n')

# printando exemplo com for, só as idades
for i in exemplo:
    print(i[1])
print('\n')

for i in exemplo:
    print(f'{i[0]} tem {i[1]} anos')
print('\n')

# inserido informações nas listas dentro de listas usando o for
dado = []
dados = []

for i in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    dados.append(dado[:])

    # Limpando os dados para o próximo laço
    dado.clear()

print(dados)

# Usando condicional de listas dentro de listas
for i in dados:
    if i[1] >= 18:
        print(f'O {i[0]} é maior de idade')

    else:
        print(f'{i[0]} é menor de idade')
