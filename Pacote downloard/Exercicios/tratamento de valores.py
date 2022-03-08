numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número inteiro. Digite 999 para sair: '))

    if numero != 999:
        soma += numero
        contador += 1

print('A soma foi: {}'.format(soma))
print('A quantidade de números foi: {}'.format(contador))