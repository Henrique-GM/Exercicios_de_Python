# PARTE 1-------------------------------------------------------------------------------------------------------------------------------

# Espreções regulares é como se fosse uma linguágem de programação e possui recursos muito interessantes para trabalhar com strings
# como pesquisa e substituição

# "RegEx" serve para encontrar todas as ocorrências de uma determinada String em outra String, ou, caracter. Retarna para nós, uma coleção com 
# esses retornos.

import re #RegEx

texto = "Curso de Python"

resposta = re.findall("Python", texto); # O que quero pesquisar e aonde
print(resposta)

pesquisa = input("Pesquisar: ")

resposta2 = re.findall(pesquisa, texto);
print(resposta2)

quantidade = len(resposta2)

print("Quantidade: " + str(quantidade))

print("\n")

# PARTE 2-------------------------------------------------------------------------------------------------------------------------------

# "re.search()" é uma função do RegEx para pesquisar Strings, por exemplo o fim e o início de uma String pesquisada.

resposta3 = re.search("Python", texto)

if(resposta3 != None): # Se não encontra o sistema identifica como None
    parte_inicial = resposta3.start() 
    parte_final = resposta3.end()

    tamanho = parte_final - parte_inicial

    print(resposta3.start())
    print(resposta3.end())

    print(tamanho)

else:
    print("Não encontrado")

print("\n")

# PARTE 3-------------------------------------------------------------------------------------------------------------------------------

# Função "Split()" divide uma String e retornar uma coleção coleção com os elementos divididos dessa String
 # O caractere que seja o divisor  " " e aonde ira procurá-lo "texto"
resposta4 = re.split(" ", texto)
print(resposta4)

# Usando o Split() para imprimir na posição escolhida
print(resposta4[2])

# imprimindo toda coleção
for i in resposta4:
    print(i)

print("\n")

# PARTE 4-------------------------------------------------------------------------------------------------------------------------------

# A função "sub()" faz uma substituição em um determinado tipo de caractere em uma String
# Substituir " " por "-" na String "texto"
resposta5 = re.sub(" ","-", texto) 
print(resposta5)



