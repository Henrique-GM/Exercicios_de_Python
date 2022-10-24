i = 1
multiplicador = 1

numero = int(input('Digite um número: '))

while numero >= i:

    multiplicador *= numero

    numero = numero - i

print(multiplicador)
