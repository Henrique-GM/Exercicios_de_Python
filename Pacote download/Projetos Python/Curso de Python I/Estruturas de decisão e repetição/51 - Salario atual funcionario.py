ano_contratado = int(input('Digite o ano que foi contratado: '))
salario = float(input('Digite seu salario de quando foi contratado: '))

for i in range(ano_contratado, 2022 + 1):
    if ano_contratado <= 1995:
        salario += (salario * 1.5 / 100)

    elif ano_contratado >= 1997:
        salario += (salario * 10 / 100)

print(f'O salário atual do funcionário é: {salario:.2f}')
