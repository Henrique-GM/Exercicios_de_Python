contador = 0
soma = 0
while True:
    numero = int(input('Digite um número(digite 999 para sair): '))

    if numero != 999:
        soma += numero
        contador += 1

    if numero == 999:
        break

print(f'Foram digitados {contador} e sua soma foi {soma}')