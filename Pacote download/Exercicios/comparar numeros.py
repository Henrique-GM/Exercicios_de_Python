numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print('Número {} é maior que {}'.format(numero1, numero2))

elif numero2 > numero1:
    print('O número {} é maior que {}'.format(numero2, numero1))

else:
    print('Os números são iguais')
    