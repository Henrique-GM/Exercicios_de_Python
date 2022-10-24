n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('\n')

maximo = max(n1, n2, n3)
minimo = min(n1, n2, n3)

print(minimo)

if n1 != maximo and n1 != minimo:
    print(n1)

elif n2 != maximo and n2 != minimo:
    print(n2)

elif n3 != maximo and n3 != minimo:
    print(n3)

print(maximo)
