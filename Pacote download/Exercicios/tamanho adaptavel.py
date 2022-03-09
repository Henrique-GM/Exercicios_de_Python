def escreva(frase):
    tamanho = len(frase)
    linhas = ('~' * (tamanho + 1))

    print(linhas)
    print(frase)
    print(linhas)


frase = str(input('Digite uma frase: '))

print()

escreva(frase)
