l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))
print('\n')

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É um triângulo')

    if l1 == l2 == l3:
        print('É um triângulo equilátero')

    elif l1 != l2 != l3:
        print('É um triângulo escaleno')

    else:
        print('É um triângulo isosceles')
