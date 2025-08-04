# impotando biblioteca do sqlite3
import sqlite3
from sqlite3 import Error # Para tratamento de erros no sqlite3


#########CRIAR CONEXÃO
# Uma função para manipulação de banco de dados, deixa o trabalho mais fácil
def ConexaoBanco():
    # Obtendo o caminho
    caminho = r'D:\curso Python\SQLite, Banco de dados e tabelas - 27\Banco.db'
    # Uma variável de conexão iniciado com o valor None
    conexao = None

    try:
        # tentativa de realizar a conexão com o sqlite.
        conexao = sqlite3.connect(caminho)
    
    # Caso não ocorra a conexão
    except Error as erro:
        print(erro)
    
    return conexao

vconexao = ConexaoBanco()

#########CRIAR TABELA
# Três aspas é para manter a formatação, para não dar erro
TabelaContatos = """CREATE TABLE tb_contatos(
                        N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
                        T_NOMECONTATO TEXT(30),
                        T_TELEFONECONTATO TEXT(14),
                        T_EMAILCONTATO TEXT(30)
                    );"""

# Para criar uma tabela precisamos passar a conexão e o comando sql
def CriarTabela(conexao, sql):
    try:
        # O cursos será respnsável por andar em nossa conexão.
        # Com o 'cursor' podemos executar o comando sql
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela criado")
    
    except Error as erro:
        print(erro)

CriarTabela(vconexao, TabelaContatos) 

vconexao.close()
