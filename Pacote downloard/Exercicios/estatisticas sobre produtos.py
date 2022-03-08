produto_mais_barato = ''
mais_barato = 0
auxiliar = 0
total = 0
contador = 0

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    escolha = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

    if auxiliar == 0:
        mais_barato = preco
        auxiliar += 1

    if preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = produto

    total += preco

    if preco > 1000:
        contador += 1

    if escolha == 'N':
        break

print(f'\nO total gasto foi {total}')
print(f'{contador} produto(os) custando mais de 1000.00')
print(f'O produto mais barato foi o(a) {produto_mais_barato} que custa {mais_barato}')
