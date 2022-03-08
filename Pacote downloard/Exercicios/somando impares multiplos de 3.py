soma = 0
contador = 0
for i in range(1, 500 + 1):

    if i % 2 != 0 and i % 3 == 0:
       print(i)
       soma += i
       contador += 1

print('\nA soma de todos os valores impares e multiplos de 3 são: {}'.format(soma))
print('A quantidade de números são: {}'.format(contador))