contador_par = 0
contador = 0

while True:
    numero = int(input('Digite um número: '))

    if numero != 1000:
        contador += 1

    if numero % 2 == 0:
        print('É par')
        contador_par += 1

    if numero % 2 != 0:
        print('É impar')

    if numero == 1000:
        break

print(f'A quantidade de pares nos números digitados são {contador_par}.\n'
      f'E o número de dados lidos são {contador}')
