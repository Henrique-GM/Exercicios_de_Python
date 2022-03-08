vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('significado', 'imprescindivel', 'perseveranca', 'inerente', 'empatia', 'perspicaz', 'dicionario',
            'peculiar', 'amor', 'perspectiva', 'denegrir', 'embuste', 'conjuge', 'condescendente', 'reciproco',
            'respeito')

sequencia = 0
for i in range(0, len(palavras[sequencia])):
    if palavras[sequencia] in vogais[0] or vogais[1] or vogais[2] or vogais[3] or vogais[4]:

        contado1 = palavras[sequencia].count('a')
        contado2 = palavras[sequencia].count('e')
        contado3 = palavras[sequencia].count('i')
        contado4 = palavras[sequencia].count('o')
        contado5 = palavras[sequencia].count('u')

        if contado1 > 0:
            contado1 = 'a'

        if contado2 > 0:
            contado2 = 'e'

        if contado3 > 0:
            contado3 = 'i'

        if contado4 > 0:
            contado4 = 'o'

        if contado5 > 0:
            contado5 = 'u'

        if contado1 == 0:
            contado1 = ''

        if contado2 == 0:
            contado2 = ''

        if contado3 == 0:
            contado3 = ''

        if contado4 == 0:
            contado4 = ''

        if contado5 == 0:
            contado5 = ''

        print(f'Na palavra "{palavras[sequencia]}" temos as vogais {contado1, contado2, contado3, contado4, contado5}')

        sequencia += 1

# Segunda forma de fazer
for i in palavras:
    print(f'\nNa palavra "{i}" temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
