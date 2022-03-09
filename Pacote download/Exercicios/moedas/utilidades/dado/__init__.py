def leiaDinheiro(numero):
    valido = False

    while not valido:
        entrada = str(input(numero))

        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: {entrada} é preço válido')

        else:
            valido = True
            return float(entrada.replace(',', '.'))
