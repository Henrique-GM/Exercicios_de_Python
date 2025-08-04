# Chave/Key - Valor/Value

carro = {
    "Fabricante" : "Honda", # chave = Fabricante / valor = Honda
    "Modelo" : "HRV",
    "Ano" : "2016",
    "Cor" : "Prata"
}

fabricante = (carro["Fabricante"])  # usando a chave para mostrar o valor.

fabricante = carro.get("Fabricante") # uma outra forma de fazer o mesmo que a linha 10.

print(fabricante)

carro["Cor"] = "Preto" # mudando diretamente o valor da matriz.

for x in carro: # mostrando apenas as chaves.
   print(x)

for x in carro: # mostrando apenas os valores.
   print(carro[x])

for chave, valor in carro.items(): #mostrando apenas as chaves e valores.
    print(chave + ": " + valor)

if "Modelo" in carro: # verificando no if atravéz do in a existência de Modelo
    print("Modelo encontrado")

for chave, valor in carro.items(): # usando o .items pode acessar os valores e chaves.
    print(chave + ": " + valor)

print("Tamanho do dicionário: " + str(len(carro))) # conta os elementos dos dicionários

carro["Cambio"] = "Automático" # incerindo elementos de chave e valor diretamente.

carro.pop("Cambio") # retirando às inormações relacionadas ao cambio.
# del carro["Cambio"] # faz a mesma coisa que a linha 37.

# carro.clear() # limpa todas as informações de carro.

carros = { # Em um único dicionário. Vários dicionários.
    "Carro1" : {
        "Fabricante" : "Honda",
        "Modelo" : "HRV"
    },

    "Carro2" : {
        "Fabricante" : "Volkswagem",
        "Modelo" : "Golf"
    },

    "Carro3" : {
        "fabricante" : "Ford",
        "Modelo" : "Focus"
    }
}

print(carros["Carro1"]["Fabricante"]) # Mostrando dicionário interno.

Carro4 = {
    "Fabricante" : "Honda",
    "Modelo" : "HRV"
}

Carro5 = {
    "Fabricante" : "Volkswagem",
    "Modelo" : "Golf"
}

Carro6 = {
    "fabricante" : "Ford",
    "Modelo" : "Focus"
}

Carros = { # Atribuindo as variáveis dicionários.
    "C1" : Carro4,
    "C2" : Carro5,
    "C3" : Carro6,
}

print(Carros["C1"])
