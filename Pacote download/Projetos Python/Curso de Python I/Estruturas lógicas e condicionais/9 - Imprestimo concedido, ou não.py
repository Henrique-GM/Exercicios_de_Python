salario = float(input('Digite seu salário: '))
emprestimo = float(input('Digite a quantidade do empréstimo: '))
print('\n')

porcentagem_limite = salario * 20 / 100

if emprestimo > porcentagem_limite:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
