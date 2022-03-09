frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')

inverter = frase[::-1]

if frase == inverter:
    print('É palindromo')

else:
    print('Não é palindromo')