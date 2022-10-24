salario_base = float(input('Digite seu salário base: '))
print('\n')

salario_base += (salario_base * 5 / 100)
imposto_salario_base = salario_base * 7 / 100

print(f'O salário do funcionário será: {salario_base - imposto_salario_base}')
