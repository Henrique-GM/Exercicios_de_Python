frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira aparição de "A" foi {}'.format(frase.find('A') + 1))
# Iniciando a procura pelo caractere pelo lado direito
print('A última aparição de "A" foi {}'.format(frase.rfind('A') + 1))
