nota1 = float('Digite sua primeira nota: ')
nota2 = float('Digite sua segunda nota: ')

media = (nota1 + nota2) / 2

if media == 5:
    print('REPROVADO')

elif media > 5 and media < 6.9:
    print('RECUPERAÇÃO')

elif media >= 7.0:
    print('APROVADO')