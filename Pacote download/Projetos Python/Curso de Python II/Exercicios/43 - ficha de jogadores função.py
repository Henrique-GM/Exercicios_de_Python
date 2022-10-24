def ficha(nome, gols):
    if nome.isalpha() == True and gols.isnumeric() == True:
        print(f'O jogador {nome} fez {gols} gol(s)')

    elif nome.isalpha() == False and gols.isnumeric() == False:
        print(f'O jogado <desconhecido> fez 0 gol(s)')

    elif nome.isalpha() == True and gols.isnumeric() == False:
        print(f'O jogador {nome} fez 0 gol(s)')

    else:
        print(f'O jogador <desconhecido> fez {gols} gol(s)')


nome = (input('Digite o nome do jogador: ')).strip()
gols = (input('Digite a quantidade feito pelo jogador: ')).strip()

ficha(nome, gols)
