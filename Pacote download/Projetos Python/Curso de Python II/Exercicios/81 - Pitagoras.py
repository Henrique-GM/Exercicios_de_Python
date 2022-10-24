from math import sqrt, hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))

print('A hipotenusa ficou: {:.2f}'.format(hipotenusa))

# Usando outra função
hipotenusa2 = hypot(cateto_oposto, cateto_adjacente)
print('{:.2f}'.format(hipotenusa2))