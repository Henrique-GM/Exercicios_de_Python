carros = [ # Array multi-dimencional.
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2025]
]

#carros.append(["Cor", "Prata"]) # Adicionando a matriz novos elementos.

# carros[2][1] = 2019 # Substituindo um valor da matriz.

# print(carros[1][1] + "\n") # Mostrando um valor na posição.

for l, c in carros:
    print(l + " | " + str(c))

