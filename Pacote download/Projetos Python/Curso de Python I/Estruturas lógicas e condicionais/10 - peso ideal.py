peso = float(input('Digite seu peso: '))
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
altura = float(input('Digite sua altura: '))

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58

    print(f'Seu peso ideal é {peso_ideal:.2f}')

elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7

    print(f'Seu peso ideal é {peso_ideal:.2f}')
