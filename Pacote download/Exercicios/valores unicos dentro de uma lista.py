valores = []
while True:
    numero = int((input('Digite um número: ')))

    if numero not in valores:
        valores.append(numero)

    else:
        print(input('Número já existente,não vou adicionar'))

    resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

    if resposta != 'S':
        break

valores.sort()
print(valores)
