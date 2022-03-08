#PRIMEIRA FORMA DE FAZER

#informacoes_pessoas = {}
#lista_dados = []
#lista_informacoes = []

#contador = 0
#media = 0

#while True:
#    informacoes_pessoas['nome'] = str(input('Digite seu nome: '))
#    informacoes_pessoas['sexo'] = str(input('Digite seu sexo: ')).strip().upper()[0]

#    print(informacoes_pessoas)

#    while informacoes_pessoas['sexo'] not in 'MF':

#        if informacoes_pessoas['sexo'] not in 'MF':
#            informacoes_pessoas['sexo'] = str(input('Digitado errado. Digite [M ou F]: ')).strip().upper()

#    informacoes_pessoas['idade'] = int(input('Digite sua idade: '))

#    lista_dados.append(informacoes_pessoas['nome'])
#    lista_dados.append(informacoes_pessoas['sexo'])
#    lista_dados.append(informacoes_pessoas['idade'])

#    lista_informacoes.append(lista_dados[:])
#    lista_dados.clear()

#    contador += 1

#    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

#    while True:
#        if escolha not in 'SN':
#            escolha = str(input('informado errado. Digite [S/N]: ')).strip().upper()

#        elif escolha in 'SN':
#            break

#    if escolha == 'N':
#        break

#for i in range(0, contador):
#    media += (lista_informacoes[i][2]) / contador

#print('-=' * 15)
#print(f'Foram cadastradas {contador} pessoas')
#print(f'A média da idade do grupo foi {media:.2f}')

#print('-=' * 15)
#for i in range(0, contador):

#    if 'F' in lista_informacoes[i]:
#        print(f'lista de informações de mulheres: {lista_informacoes[0][0]}')

#print('-=' * 15)
#for i in range(0, contador):

#    if lista_informacoes[i][2] > media:
#        print(f'lista de pessoas com idade maior que a média: {lista_informacoes[i]}')

# OUTRO JEITO

pessoa = dict()
galera = list()
soma = 0
media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]

        if pessoa['sexo'] in 'MFmf':
            break

        print('Por favor digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if resposta in 'SNsn':
            break

        print('Responda apenas [S/N]')

        if resposta == 'SNsn':
            break

    if resposta == 'N':
        break

print('-=' * 30)
print(f'Temos {len(galera)} pessoas cadastradas')

media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos')

print('A mulheres cadastradas foram ', end='')
# Buscando dentro da lista, pelos dicionários
for i in galera:
    if i['sexo'] in 'Ff':

        print(f'{i["nome"]}', end=' ')

# Evitar que às saídas se juntem
print()

print('Pessoas com a idade acima da média: ', end='')
for i in galera:
    if i['idade'] > media:

        for chave, valor in i.items():
            print(f'{chave} = {valor}', end='//')

