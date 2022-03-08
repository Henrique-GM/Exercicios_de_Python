from codigos import dados
from codigos import Arquivos
from time import sleep

arquivo = 'teste.txt'

if not Arquivos.arquivoExiste(arquivo):
    Arquivos.criarArquivo(arquivo)

while True:
    resposta = dados.menu(['Ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistema'])

    if resposta == 1:
        print('-' * 30)

        Arquivos.lerArquivo(arquivo)

        print('-' * 30)

    elif resposta == 2:
        print('-' * 30)
        print('        NOVO CADASTRO')
        print('-' * 30)
        print()

        nome = str(input('Nome: '))
        idade = dados.leiaInt('Digite a idade: ')
        Arquivos.cadastrar(arquivo, nome, idade)

        print('-' * 30)

    elif resposta == 3:
        print('-' * 30)
        print('Saindo do sistema... Até logo')
        print('-' * 30)
        break

    else:
        print('-' * 30)
        print('Erro na digitação')
        print('-' * 30)

    sleep(2)
