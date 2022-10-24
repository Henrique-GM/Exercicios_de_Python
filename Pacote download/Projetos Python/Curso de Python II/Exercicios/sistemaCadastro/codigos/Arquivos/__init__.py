def arquivoExiste(nome):
    try:
        # a função open tenta abrir um arquivo
        # rt. ler arquivo em modo txt
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criarArquivo(nome):
    try:
        # wt. Escreve um arquivo de texto
        # +. Se por acaso o arquivo não existir, ele cria
        a = open(nome, 'wt+')
        a.close()

    except:
        print('Houve um erro na criação do arquivo')

    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('Erro ao ler arquivo')

    else:
        print('     PESSOAS CADASTRADAS')
        print('    ---------------------')
        # ler documento
        print(a.read())

    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        # at. Significa append, ou seja, por dados
        a = open(arquivo, 'at')

    except:
        print('Houve um erro na abertura do arquivo')

    else:
        # write. Para a informação ser escrita
        try:
            a.write(f'{nome};{idade}\n')

        except:
            print('Houve um ERRO na hora de escrever os dados')

        else:
            print(f'Novo registros de {nome} adicionado')
            a.close()
