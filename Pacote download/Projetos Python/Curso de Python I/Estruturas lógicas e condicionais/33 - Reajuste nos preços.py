preco = float(input('Digite o preço: '))

if preco <= 50:
    preco += (preco * 5 / 100)

    print(f'O reajuste foi de 5% que deu {preco}')

    if preco <= 80:
        print('barato')
    elif preco > 80 and preco < 120:
        print('normal')
    elif preco > 120 and preco < 200:
        print('caro')
    elif preco > 200:
        print('muito caro')

elif preco > 50 and preco < 100:
    preco += (preco * 10 / 100)

    print(f'O reajuste foi de 10% que deu {preco}')

    if preco <= 80:
        print('barato')
    elif preco > 80 and preco < 120:
        print('normal')
    elif preco > 120 and preco < 200:
        print('caro')
    elif preco > 200:
        print('muito caro')

elif preco > 100:
    preco += (preco * 15 / 100)

    print(f'O reajuste foi de 15% que deu {preco}')

    if preco <= 80:
        print('barato')
    elif preco > 80 and preco < 120:
        print('normal')
    elif preco > 120 and preco < 200:
        print('caro')
    elif preco > 200:
        print('muito caro')
