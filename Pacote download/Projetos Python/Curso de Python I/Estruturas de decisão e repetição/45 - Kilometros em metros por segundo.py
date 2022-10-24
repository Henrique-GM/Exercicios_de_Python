while True:
    escolha = str(input('Digite K para converter m/s para Km/h'
                        'ou M para converte Km/h para m/s: ')).upper().strip()[0]
    print('\n')

    if escolha == 'K':
        ms = float(input('Digite em metros em M/S: '))
        k = ms * 3.6
        print(f'O resultado foi {k:.2f}')

    if escolha == 'M':
        k = float(input('Digite em km/h: '))
        ms = k / 3.6
        print(f'O resultado foi {ms:.2f}')

    repete = str(input('Digite S para repetir e N para não repetir: ')).upper().strip()[0]

    while repete != 'S' and repete != 'N':
        repete = str(input('Digite S para repetir e N para não repetir: ')).upper().strip()[0]

    if repete == 'N':
        break
