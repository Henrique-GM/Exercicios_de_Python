distancia_KM = float(input('Digite a distancia em KM: '))
litros_consumidos = float(input('Digite o consumo médio de litros de combustível consumidos pelo carro: '))
print('\n')
consumo = distancia_KM / litros_consumidos

if consumo < 8:
    print('Venda o carro')

elif consumo > 8 and consumo < 14:
    print('Econômico')

elif consumo > 12:
    print('Super econômico')
