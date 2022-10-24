trabalho_laboratorio = int(input('Digite a nota que recebeu (0 a 10): '))
avaliacao_semestral = int(input('Digite a nota que recebeu (0 a 10): '))
exame_final = int(input('Digite a nota que recebeu (0 a 10): '))
print('\n')

media_ponderada = (trabalho_laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)
media_ponderada /= 10

print(media_ponderada)

if media_ponderada == 0 or media_ponderada <= 2.9:
    print('Reprovado')

elif media_ponderada == 3 or media_ponderada <= 4.9:
    print('Recuperação')

elif media_ponderada > 4.9:
    print('Aprovado')
