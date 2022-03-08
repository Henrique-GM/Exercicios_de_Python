velocidade_carro = float(input('Digite a velocidade do autômovel: '))

if velocidade_carro > 80:
    print('Voçê foi multado. O preço da multa ficou {:.2f}'.format((velocidade_carro - 80) * 7))

else:
    print('Voçê não foi multado')
