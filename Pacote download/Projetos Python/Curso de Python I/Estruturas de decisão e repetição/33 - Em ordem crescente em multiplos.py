n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
quantidade = int(input('Digite a quantidade para os múltiplos: '))

print('\n')

while quantidade > 0:
    for i in range(0, 999):
        if i % n1 == 0 or i % n2 == 0:
            print(i, end=' ')

            quantidade -= 1

        if quantidade == 0:
            break
