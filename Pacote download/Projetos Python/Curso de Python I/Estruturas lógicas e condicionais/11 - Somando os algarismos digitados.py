numero = int(input('Digite um número inteiro de três dígitos: '))
print('\n')

if numero == 0:
    print('Número inválido')

else:
    n1 = str(numero)[0]
    n2 = str(numero)[1]
    n3 = str(numero)[2]

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    resultado = n1 + n2 + n3

    print(f'A soma dos algarismos é: {resultado}')
