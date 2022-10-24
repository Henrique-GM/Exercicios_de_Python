base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
print('\n')

while base <= 0 or altura <= 0:
    print('Digite os dados maiores e diferentes de 0')

    base = float(input('Digite a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))


area = base * altura / 2

print(f'A área do triângulo é {area:.2f}')
