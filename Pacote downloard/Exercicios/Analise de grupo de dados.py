mais_de_18 = 0
conta_masculino = 0
feminino_menos_de_20 = 0

while True:
    idade = int(input('Digite sua idade: '))

    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

    if idade > 18:
        mais_de_18 += 1

    if sexo == 'M':
        conta_masculino += 1

    if sexo == 'F' and idade < 20:
        feminino_menos_de_20 += 1

    resposta = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

    while resposta not in 'SN':
        resposta = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

    if resposta == 'N':
        break

print('\nForam cadastrados {} pessoas com mais de 18 anos'.format(mais_de_18))
print('Foram cadastrados {} homens'.format(conta_masculino))
print('Foram cadastradas {} mulheres com menos de 20 anos'.format(feminino_menos_de_20))
