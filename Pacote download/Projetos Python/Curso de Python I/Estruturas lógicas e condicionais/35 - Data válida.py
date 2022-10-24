ano = int(input('Digite o ano: '))
print('\n')

if ano % 400 == 0 or ano % 4 == 0:
    if ano % 100 != 0:

        mes = int(input('Digite o mês em número: '))
        dia = int(input('Digite o dia: '))

        if mes == 1:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 2:
            if dia > 0 and dia <= 29:
                print(f'Dia {dia} é uma data válida')

        elif mes == 3:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 4:
            if dia > 0 and dia <= 30:
                print(f'Dia {dia} é uma data válida')

        elif mes == 5:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 6:
            if dia > 0 and dia <= 30:
                print(f'Dia {dia} é uma data válida')

        elif mes == 7:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 8:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 9:
            if dia > 0 and dia <= 30:
                print(f'Dia {dia} é uma data válida')

        elif mes == 10:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        elif mes == 11:
            if dia > 0 and dia <= 30:
                print(f'Dia {dia} é uma data válida')

        elif mes == 12:
            if dia > 0 and dia <= 31:
                print(f'Dia {dia} é uma data válida')

        else:
            print('Dia inválido')

else:

    mes = int(input('Digite o mês em número: '))
    dia = int(input('Digite o dia: '))

    if mes == 1:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 2:
        if dia > 0 and dia <= 28:
            print(f'Dia {dia} é uma data válida')

    elif mes == 3:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 4:
        if dia > 0 and dia <= 30:
            print(f'Dia {dia} é uma data válida')

    elif mes == 5:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 6:
        if dia > 0 and dia <= 30:
            print(f'Dia {dia} é uma data válida')

    elif mes == 7:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 8:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 9:
        if dia > 0 and dia <= 30:
            print(f'Dia {dia} é uma data válida')

    elif mes == 10:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')

    elif mes == 11:
        if dia > 0 and dia <= 30:
            print(f'Dia {dia} é uma data válida')

    elif mes == 12:
        if dia > 0 and dia <= 31:
            print(f'Dia {dia} é uma data válida')
