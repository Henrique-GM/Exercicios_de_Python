venda_mensal = float(input('Digite o valor da venda mensal: '))
print('\n')

if venda_mensal >= 10000000:
    comissao = 700 + (venda_mensal * 16 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')

elif venda_mensal < 10000000 and venda_mensal >= 8000000:
    comissao = 650 + (venda_mensal * 14 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')

elif venda_mensal < 8000000 and venda_mensal >= 6000000:
    comissao = 600 + (venda_mensal * 14 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')

elif venda_mensal < 6000000 and venda_mensal >= 4000000:
    comissao = 550 + (venda_mensal * 14 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')

elif venda_mensal < 4000000 and venda_mensal >= 2000000:
    comissao = 500 + (venda_mensal * 14 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')

elif venda_mensal < 2000000:
    comissao = 400 + (venda_mensal * 14 / 100)

    print(f'Você recebeu de comissão {comissao:.2f}R$')
