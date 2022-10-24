maior = 0
opcao = 0

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

while opcao != 5:

    print('''
    Digite[1] para somar
    Digite[2] para multiplicar
    Digite[3] para saber o maior
    Digite[4] para ter novos números
    Digite[5] para sair do programa\n''')

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        soma = numero1 + numero2
        print(soma)

    elif opcao == 2:
        multiplicar = numero1 * numero2
        print(multiplicar)

    elif opcao == 3:

        if numero1 > numero2:
            print(numero1)
        else:
            print(numero2)

    elif opcao == 4:
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))

    else:
        print('Opção invalida')