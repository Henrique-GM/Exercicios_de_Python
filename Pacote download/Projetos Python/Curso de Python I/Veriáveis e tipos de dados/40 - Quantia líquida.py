dias_trabalhados = int(input('Quantos dias você trabalhou: '))
print('\n')

quantia_liquida = (dias_trabalhados * 30.00)
quantia_liquida -= (quantia_liquida * 8 / 100)

print(f'A quantia líquida à receber será {quantia_liquida}')
