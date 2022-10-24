n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

print('\n')
print('Digite "1" para somar\n'
      'Digite "2" para subtrair\n'
      'Digite "3" para multiplicar\n'
      'Digite "4" para dividir\n')
print('\n')

opcao = int(input('Digite uma opção: '))

if opcao == 1:
    resultado = n1 + n2
    print(f'O resultado foi: {resultado:.2f}')

elif opcao == 2:
    resultado = n1 - n2
    print(f'O resultado foi: {resultado:.2f}')

elif opcao == 3:
    resultado = n1 * n2
    print(f'O resultado foi: {resultado:.2f}')

elif opcao == 4:
    resultado = n1 / n2
    print(f'O resultado foi: {resultado:.2f}')
