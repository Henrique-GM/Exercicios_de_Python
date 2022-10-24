km = float(input('Digite a quantidade de quilômetros rodados pelo carro alugado: '))
dias = int(input('Quantos dias você alugou o carro: '))
pagar = (km * 0.15) + (dias * 60)

print('A quantidade a pagar será: {:.2f}'.format(pagar))
