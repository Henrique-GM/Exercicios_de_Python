# PARTE 1 ---------------------------------------------------------------------------------------------
import json

# Entre apostrofes que vai ser a nossa string para o json
# Para o Python é parecido com o dicionário. Consigo manipular o json, como se manipula um dicionário
carros_json = '{"marca" : "honda", "modelo" : "HRV", "cor" : "prata"}'

# O "loads" carrega o json e trasformar esse elemento já em uma string. Bem parecido com um dicionário
carros = json.loads(carros_json)

# Imprime somento o valor de marca.
print(carros["marca"])
print(carros["modelo"])

# Imprime somente as chaves
for x in carros:
    print(x)

print("\n")

# Imprime somente os valores
for x in carros.values():
    print(x)

print("\n")

# Imprime somente os itens
for x in carros.items():
    print(x)

print("\n")

# Imprime somente os itens
for k,v in carros.items():
    print(k + " - " + v) 

print("\n")

# Um dicionário
carros2 = {
        "marca" : "honda", 
        "modelo" : "HRV", 
        "cor" : "prata"
}

# Converção de dicionário para json
carros_json_2 = json.dumps(carros2)

print(carros_json_2)

print("\n")

# PARTE 2 ---------------------------------------------------------------------------------------------

carros_dicionario = {
        "marca" : "honda", 
        "modelo" : "HRV", 
        "cor" : "prata"
}

# Dicionario. objeto json
jogador = '{"nome" : "Bruno", "time" : "aviadores", "vivo" : "True", "energia" : 100, "mochila" : ["pederneira", "corda", "linha", "arame"], "aeronaves" : [{"tipos": "transporte", "habilidade" : 80}, {"tipos": "ataque", "habilidade" : 100}, {"tipos": "reconhecimento", "habilidade" : 50}]}'

carros_list = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]
# Lista. Array json

carros_tupla = ("honda", "volkswagem", "ford", "fiat", "chevrolet")
# Tupla. Array json

# Podemos converter dicionários, listas e tuplas 
# "indent" serve para à identação
# "separators" serve para trocarmos os separadores
# "sort_keys" Podemos ordenar as chaves
carros_j = json.dumps(carros_dicionario, indent=4, separators=(": ","="), sort_keys=True)
print(carros_j)

print("\n")

print(jogador)

print("\n")

# PARTE 3 ---------------------------------------------------------------------------------------------

# Converte o json em um elemento do python
jogador2 = json.loads(jogador)

# chaves
for c in jogador2:
    print(c)

print("\n")

# itens
for i in jogador2.items():
    print(i)

print("\n")

# valores
for v in jogador2.values():
    print(v)

print("\n")

# nome do jogador
print(jogador2["nome"])
print(jogador2["time"])

print("\n")

# Os itens da mochila
for m in jogador2["mochila"]:
    print(m)

print("\n") 

# items das aeronaves
for a in jogador2["aeronaves"]:
    print(a)

print("\n") 

# tipos das aeronaves
for a in jogador2["aeronaves"]:
    print(a["tipos"])

print("\n") 

# abilidades das aeronaves
for ab in jogador2["aeronaves"]:
    print(ab["habilidade"])

print("\n") 

# tipos e abilidades das aeronaves
for ta in jogador2["aeronaves"]:
    print(ta["tipos"] + " - " + str(ta["habilidade"]))

print("\n")

# PARTE 4 ---------------------------------------------------------------------------------------------

# Buscando o arquivo em json de forma externa
# "as" para dar um apelido
# "loud" é para conteudo externo
# Use r'' para evitar problemas com barras invertidas no caminho.
# Especifique "encoding='utf-8'" ao abrir o arquivo para evitar problemas de codificação.
# Certifique-se de que o arquivo tem a extensão .json
with open(r'D:\curso Python\JSON em PYTHON - 24\jogador.json', encoding='utf-8') as j:
    jogador3 = json.load(j)

# Iterando sobre as chaves do JSON
for c in jogador3:
    print(c)
