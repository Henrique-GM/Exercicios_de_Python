valores = []

contador = 0
while True:
    valores.append(int(input('Digite um valor: ')))

    contador += 1

    escolha = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if escolha in 'N':
        break

valores.sort(reverse=True)
print(f'\nOs valores em ordem decrescente foi: {valores}')

print(f'Foram digitados {contador}')

if 5 in valores:
    print('Tem 5')

else:
    print('Não tem 5')
