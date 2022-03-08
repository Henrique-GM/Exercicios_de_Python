numero = int(input('Digite um número inteiro qualquer: '))

resposta = int(input('Digite "1" para binário "2" para octal e "3" para hexadecimal: '))

if resposta == 1:
    print('Em binário ficou {}'.format(bin(numero)[2:]))

elif resposta == 2:
    print('Em octal ficou {}'.format(oct(numero)[2:]))

elif resposta == 3:
    print('Em hexadecimal ficou {}'.format(hex(numero)[2:]))

else:
    print('Digite somente as três opções')