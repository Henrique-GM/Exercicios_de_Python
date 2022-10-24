a = int(input('Digite o cateto: '))
b = int(input('Digite outro cateto: '))
c = int(input('Digite a hipotenusa: '))

soma = 0
soma += (a ** 2) + (b ** 2)

if soma == (c ** 2):
    print('É um terno pitagórico')
