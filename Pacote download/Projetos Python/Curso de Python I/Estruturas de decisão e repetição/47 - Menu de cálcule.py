print('MENU DE CÁLCULO')
print('\n')

print('Digite "+" para somar\n'
      'Digite "-" para subtrair\n'
      'Digite "*" para multiplicar\n'
      'Digite "/" para dividir\n'
      'Digite "S" para sair\n')
print('\n')

while True:
    opcao = str(input('Digite sua opção: '))

    if opcao == 'S':
        break

    while opcao != '+' and opcao != '-' and opcao != '*' and opcao != '/' and opcao != 'S':
        print('Digite apenas às opções mostradas')
        opcao = str(input('Digite sua opção: '))

    print('\n')
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    if opcao == '+':
        resultado = numero1 + numero2
        print(f'O resultado da soma foi: {resultado:.2f}')
    elif opcao == '-':
        resultado = numero1 - numero2
        print(f'O resultado da subtração foi: {resultado:.2f}')
    elif opcao == '*':
        resultado = numero1 * numero2
        print(f'O resultado da multiplicação foi: {resultado:.2f}')
    elif opcao == '/':
        resultado = numero1 / numero2
        print(f'O resultado da divisão foi: {resultado:.2f}')

    print('\n')
    print('Digite "+" para somar\n'
          'Digite "-" para subtrair\n'
          'Digite "*" para multiplicar\n'
          'Digite "/" para dividir\n'
          'Digite "S" para sair\n')
    print('\n')
