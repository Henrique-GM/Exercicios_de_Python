while True:
    r1 = float(input('Digite o valor do primeiro resistor: '))
    r2 = float(input('Digite o valor do segundo resistor: '))

    resistencia = (r1 * r2) / (r1 + r2)

    if resistencia == 0:
        break
