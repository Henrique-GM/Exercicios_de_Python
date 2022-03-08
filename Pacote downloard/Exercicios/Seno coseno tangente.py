from math import sqrt, sin, cos, tan, radians

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))

print(hipotenusa)

seno = cateto_oposto / hipotenusa
coseno = cateto_adjacente / hipotenusa
tangente = cateto_oposto / cateto_adjacente

print('\nSeno: {:.2f} Cosseno: {:.2f} Tangente: {:.2f}'.format(seno, coseno, tangente))

# Usando outra função

angulo = float(input('\nDigite um ângulo: '))
seno2 = sin(radians(angulo))
coseno2 = cos((radians(angulo)))
tangente2 = tan(radians(angulo))

print('Usando outra função ficou SENO:{:.2f} COSENO:{:.2f} TANGENTE:{:.2f}'.format(seno2, coseno2, tangente2))
