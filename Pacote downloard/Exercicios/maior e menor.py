numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print('O número {} é o maior'.format(numero1))

if numero2 > numero1 and numero2 > numero3:
    print('O maior número é {}'.format(numero2))

if numero3 > numero2 and numero3 > numero1:
    print('O maior número é {}'.format(numero3))

if numero1 < numero2 and numero1 < numero3:
    print('O número {} é o menor'.format(numero1))

if numero2 < numero1 and numero2 < numero3:
    print('O menor número é {}'.format(numero2))

if numero3 < numero2 and numero3 < numero1:
    print('O menor número é {}'.format(numero3))