viagem = float(input('Digite a distância da viagem em KM: '))

if viagem <= 200:
    print('O valor cobrado será: {:.2f}$'.format(viagem * 0.50))

else:
    print('O valor cobrado será: {:.2f}$'.format(viagem * 0.45))