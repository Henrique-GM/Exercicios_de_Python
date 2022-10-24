print('-='*20)
print('EMPRÉSTIMO PARA COMPRAR DE UMA CASA')
print('-='*20)

valor_casa = float(input('Qual é o valor da casa? '))
salario_comprador = float(input('Qual é o seu salário? '))
anos_pagamento = int(input('Em quantos anos você pretende pagar? '))

valor_prestacao = (valor_casa / anos_pagamento) / 12

if valor_prestacao > (salario_comprador * 30 / 100):
    print('Infelizmente não podemos realizar o empréstimo')

else:
    print('\nPodemos realizar o emprestimo')
