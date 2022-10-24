valor_pago = float(input('Digite o valor recebido: '))
print('\n')

desconto = valor_pago - (valor_pago * 10 / 100)
parcela = valor_pago / 3
comicao_vendedor_vista = desconto * 5 / 100
comicao_vendedor_parcela = valor_pago * 5 / 100

print(f'O total à pagar com 10% caso haja desconto, foi {desconto}\n'
      f'O valor de cada parcela, caso haja parcelamento de 3x sem juros {parcela}\n'
      f'Comissão do vendedor, caso seja venda à vista {comicao_vendedor_vista}\n'
      f'Comissão do vendedor, caso venda parcelada {comicao_vendedor_parcela}\n')
