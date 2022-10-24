nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
nota3 = float(input('Digite a nota da terceira prova: '))
print('\n')

media_ponderada = (nota1 * 1) + (nota2 * 1) + (nota3 * 2)
media_ponderada /= 4

if media_ponderada >= 60:
    print('Aprovado')

else:
    print('Reprovado')
