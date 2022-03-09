n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

numeros = (n1, n2, n3, n4)

print(f'\nAPARECE {numeros.count(9)} VEZ(VEZES) O NÚMERO 9')

if n1 != 3 and n2 != 3 and n3 != 3 and n4 != 3:
    print('NÃO FOI REGISTRADA A APARIÇÃO DE 3')

else:
    print(f'O PRIMEIRA APARIÇÃO DE 3 FOI NA POSIÇÃO {numeros.index(3) + 1}')

for i in numeros:
    if i % 2 == 0:
        print(f'Os números par(es) é: {i}')
