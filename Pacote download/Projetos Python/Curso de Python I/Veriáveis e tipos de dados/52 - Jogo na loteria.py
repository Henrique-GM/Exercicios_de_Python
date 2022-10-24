premio = float(input('Digite o valor do prêmio: '))

aposta_1 = float(input('Digite a porcentagem apostada: '))
aposta_2 = float(input('Digite a porcentagem apostada: '))
aposta_3 = float(input('Digite a porcentagem apostada: '))
print('\n')

print(f'O primeiro apostador receberá: {premio * aposta_1 / 100}\n'
      f'O segundo apostador receberá: {premio * aposta_2 / 100}\n'
      f'Já o terceiro apostador receberá: {premio * aposta_3 / 100}\n')
