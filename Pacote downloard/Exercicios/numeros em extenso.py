numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
                   'vinte')

escolha = int(input('Digite um número entre 0 e 20: '))

while escolha < 0 or escolha > 20:
    escolha = int(input('Digitado errado. Digite um número entre 0 e 20: '))

for i in range(0, len(numeros_extenso)):
    print(f'Você digitou: {numeros_extenso[escolha]}')
    break
