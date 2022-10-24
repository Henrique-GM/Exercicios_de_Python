altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
print('\n')

if altura < 1.20:
    if peso <= 60:
        print('A')
    elif peso > 60 and peso < 90:
        print('D')
    elif peso > 90:
        print('G')

elif altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        print('B')
    elif peso > 60 and peso < 90:
        print('E')
    elif peso > 90:
        print('H')

elif altura > 1.70:
    if peso <= 60:
        print('C')
    elif peso > 60 and peso < 90:
        print('F')
    elif peso > 90:
        print('I')
