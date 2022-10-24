Chico = 1.50
Ze = 1.10
ano = 0

while True:
    Chico += 0.2
    Ze += 0.3

    if Ze > Chico:
        break

    ano += 1

print(f'Foram necessários {ano} anos para Zé ficar maior que o Chico')
