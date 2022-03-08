dados = []
informacaoes = []
contador = 0
maior = 0
menor = 0
auxiliar = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))

    informacaoes.append(dados[:])
    dados.clear()

    contador += 1

    resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

    if resposta == 'N':
        break

print(f'Temos {contador} pessoas cadastradas')

for i in informacaoes:
    if auxiliar == 0:
        maior = i[1]
        menor = i[1]
        auxiliar += 1

    elif i[1] > maior:
        maior = i[1]

    elif i[1] < menor:
        menor = i[1]

print(f'O maior peso de {maior} é de ', end='')

for i in informacaoes:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')

print(f'\nO menor peso de {menor} é de ', end='')

for i in informacaoes:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')
