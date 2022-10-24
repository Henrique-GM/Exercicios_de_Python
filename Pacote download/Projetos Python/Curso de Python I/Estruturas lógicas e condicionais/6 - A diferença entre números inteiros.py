numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
print('\n')

if numero1 > numero2:
    print(f'O maior número entre os dois é {numero1} e a diferença entre eles é de {numero1 - numero2} números')
else:
    print(f'O maior número entre os dois é {numero2} e a diferença entre eles é de {numero2 - numero1} números')
