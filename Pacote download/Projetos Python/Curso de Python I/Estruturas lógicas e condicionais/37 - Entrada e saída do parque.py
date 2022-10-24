horas_entrada = int(input('Digite às horas em que chegou ao parque: '))
minutos_entrada = int(input('Digite os minutos em que chegou ao parque: '))

print('\n')

horas_saida = int(input('Digite às horas em que chegou ao parque: '))
minutos_saida = int(input('Digite os minutos em que chegou ao parque: '))

horas = horas_saida - horas_entrada
minutos = minutos_saida + minutos_entrada

if minutos > 60:
    horas += 1

if horas > 24:
    print('Parque fechado')

print('\n')

if horas < 24:
    if horas >= 1 and horas <= 2:
        print(f'1 real por hora cada que dá {1 * horas:.2f}')

    elif horas >= 3 and horas <= 4:
        print(f'1.4 reis por hora cada que dá {1.4 * horas:.2f}')

    elif horas >= 5:
        print(f'2.0 R$ reais por hora cada que dá {2.0 * horas:.2f}')
