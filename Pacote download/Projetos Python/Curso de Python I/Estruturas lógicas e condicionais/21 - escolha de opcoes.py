n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

print('\n')
print('Digite "1" para soma os dois números\n'
      'Digite "2" para diferença entro os dois números (maior pelo menor)\n'
      'Digite "3" para obter o produto dos dois números\n'
      'Digite "4" para dividir um número pelo outro (o denominador não pode ser zero)\n')
print('\n')

opcao = int(input('Digite sua escolha: '))

if opcao == 1:
    print(f'A soma ficou {n1 + n2}')

elif opcao == 2:
    if n1 > n2:
        print(f'A diferença entre os dois números é {n1 - n2}')
    else:
        print(f'A diferença entre os dois números é {n2 - n1}')

elif opcao == 3:
    print(f'O produto dos dois números é {n1 * n2}')

elif opcao == 4:
    if n2 == 0:
        print('O denominador não pode ser zero')
    else:
        print(f'A divisão entre esses números é {n1 / n2:.2f}')

else:
    print('Erro na digitação')
