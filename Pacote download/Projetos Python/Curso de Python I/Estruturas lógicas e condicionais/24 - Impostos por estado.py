valor_produto = float(input('Digite o valor do produto: '))
estado_destino = str(input('Digite a sigla do estado destino do produto: ')).strip().upper()
print('\n')

if estado_destino == 'MG':
    valor_produto += (valor_produto * 7 / 100)
    print(f'O valor do produto em MG é {valor_produto}')

elif estado_destino == 'SP':
    valor_produto += (valor_produto * 12 / 100)
    print(f'O valor do produto em SP é {valor_produto}')

elif estado_destino == 'RJ':
    valor_produto += (valor_produto * 15 / 100)
    print(f'O valor do produto em RJ é {valor_produto}')

elif estado_destino == 'MS':
    valor_produto += (valor_produto * 12 / 100)
    print(f'O valor do produto em MS é {valor_produto}')

else:
    print('Esse estado não está na lista')
