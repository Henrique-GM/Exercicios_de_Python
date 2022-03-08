preco = float(input('Digite o preço do produto: '))
desconto = (preco * 5) / 100

print('O novo preço do produto com 5% de desconto foi: {:.2f}'.format(preco - desconto))
