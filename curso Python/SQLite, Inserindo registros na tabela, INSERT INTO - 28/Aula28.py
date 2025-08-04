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

# incerindo dados atravez do input
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

#########CRIAR TABELA
# Três aspas é para manter a formatação, para não dar erro
vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        # Para fazer a persistencia dos dados é preciso comitar.
        conexao.commit()
        print("Registro incerido")
    
    except Error as erro:
        print(erro)

inserir(vconexao, vsql)

