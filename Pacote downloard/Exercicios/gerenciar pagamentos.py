preco_produto = float(input('Digite o preço do produto: R$ '))
condicao_pagamnto = int(input('"1" para a vista em dinheiro ou em cheque'
                              '\n"2" para a vista no cartão\n"3" para 2 vezez no cartão'
                              '\n"4" para 3x ou mais no cartão\n'))

if condicao_pagamnto == 1:
    print('Com 10% de deconto sua conta ficou: {:.2f}'.format(preco_produto - (preco_produto * 10 / 100)))

elif condicao_pagamnto == 2:
    print('Com 5% de desconto sua conta ficou: {:.2f}'.format(preco_produto - (preco_produto * 5 / 100)))

elif condicao_pagamnto == 3:
    print('Sua conta permanece o preço normal: {:.2f}'.format(preco_produto))

elif condicao_pagamnto == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Com {} parcelas o valor ficou: R$ {}'.format(parcelas, preco_produto / parcelas))

    print('Com 20% de juros sua conta ficou: {:.2f}'.format(preco_produto + (preco_produto * 20 / 100)))
