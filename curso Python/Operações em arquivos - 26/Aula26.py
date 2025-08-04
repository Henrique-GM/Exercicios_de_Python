import re
import os

# PARTE 1 ----------------------------------------------------------------------------------------------------------------------------------

# Usaremos o "open()" para fazer a abertura do arquivo e verificar se esse arquivo existe, se não existir pode criar e existe várias formas
# de abertura desse arquivo.

nome = "teste.txt"

# Variável/caminho do arquivo/nome do arquivo/função que deseja no arquivo
arquivo = open(r'D:/curso Python/Operações em arquivos - 26/' + nome, "a")

# r - read - Leitura
# a - append - Anexar algo a mais no arquivo
# w - write - Escrita, e caso não tenha o arquivo, será criado
# x - create - criar
# t - text - texto (Padrão) podemos omitir.
# b - binary - binário - usado para escrever caracteres em modo binário, dentro de arquivos de imagens convertendo o String para binário 
    # e mandá-lo para dentro de outro arquivo

#txt = input("Digite um texto: ")
#arquivo.write(txt + "\n")

# IMPORTANTE. Para não ter arquivo na memória ou execução do programa.
arquivo.close()

# PARTE 2 ----------------------------------------------------------------------------------------------------------------------------------

arquivo2 = open(r'D:/curso Python/Operações em arquivos - 26/' + nome, "r")

# print de leitura dos primeiros 5 caracteres
#print(arquivo2.read(5)) 

#print(arquivo2.readline()) # A função readline pode ler as linhas. Lê primeira linha. Retorna uma String
#print(arquivo2.readline()) # Lê segunda linha.

# Quando se não sabe quantos aruivos são, recomendo usar o FOR
#for i in arquivo2:
#   print(i)

# Manipulando informações em um arquivo.
# No arquivo não muda no modo "r", somente na impreção na variável "resposta"
resultado = re.sub(" ", "-", arquivo2.readline())
print(resultado)

# O arquivo muda no modo "w" e a utilização do write. 
arquivo2 = open(r'D:/curso Python/Operações em arquivos - 26/' + nome, "w")
arquivo2.write(resultado)


arquivo2.close()

# PARTE 3 ----------------------------------------------------------------------------------------------------------------------------------

caminho = r'D:/curso Python/Operações em arquivos - 26/'



# Para identificar a existencia do arquivo e criá-lo
if os.path.exists(caminho + nome):
    print("Arquivo existente")
else:
    arquivo3 = open(caminho + nome, "x")

    arquivo3.close()

# Para identificar a existencia do arquivo e apagá-lo
if os.path.exists(caminho + nome):
    os.remove(caminho + nome)
else:
    print("Arquivo inexistente")


# Para remover arquivos.
#os.remove(caminho + nome)