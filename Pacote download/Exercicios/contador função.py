def escolha_do_usuario(inicio, fim, passo):

    for i in range(inicio, fim - 1, passo):
        print(i, end=' ')


def um_a_dez():
    for i in range(1, 10 + 1, 1):
        print(i, end=' ')


def dez_a_zero():
    for i in range(10, 0 - 1, -2):
        print(i, end=' ')
    print()


um_a_dez()
print()
dez_a_zero()

inicio = int(input('Digite o valor do início: '))
fim = int(input('Digite o valor do fim: '))
passo = int(input('Digite o valor do passo: '))

print()

escolha_do_usuario(inicio, fim, passo)
