salario = float(input('Digite seu salário: '))

if salario > 1200:
    salario = salario + ((salario * 10) / 100)
    print('O aumento do salário ficou ${}'.format(salario))

if salario < 1200:
    salario = salario + ((salario * 15) / 100)
    print('O aumento do salário ficou ${}'.format(salario))