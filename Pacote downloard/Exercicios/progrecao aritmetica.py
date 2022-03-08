primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro_termo
contado = 1

mais = 10
total = 0
while mais != 0:
    total += mais
    while contado <= total:
        print(termo)
        termo += razao
        contado += 1

    mais = int(input('Quantos termos voçê quer: '))

    if mais == 0:
        break
