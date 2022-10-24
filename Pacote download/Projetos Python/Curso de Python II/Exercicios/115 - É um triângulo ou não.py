angulo1 = float(input('Digite o primeiro angulo: '))
angulo2 = float(input('Digite o segundo angulo: '))
angulo3 = float(input('Digite o terceiro angulo: '))

if angulo2 + angulo3 > angulo1 and angulo1 + angulo3 > angulo2 and angulo1 + angulo2 > angulo3:
    print('\nÉ um triângulo')

    if angulo1 == angulo2 == angulo3:
        print('\nÉ equilátero')

    elif angulo1 == angulo2 != angulo3 or angulo1 == angulo3 != angulo2 or angulo3 == angulo2 != angulo1:
        print('\nisósceles')

    elif angulo1 != angulo2 != angulo3:
        print('\nEscaleno')

else:
    print('Não é um triângulo')

