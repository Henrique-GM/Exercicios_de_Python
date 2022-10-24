valor = int(input('Qual valor você quer sacar? R$'))

total = valor
cedula = 100
total_de_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_de_cedulas += 1

    else:
        if total_de_cedulas > 0:
            print(f'Total de {total_de_cedulas} cédulas de R${cedula}')

        elif cedula == 100:
            cedula = 50

        elif cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 2

        total_de_cedulas = 0

        if total == 0:
            break
