tupla_carros = ("HRV", "Golf", "Argo") # uma tupla não permite mudança direta dos seus elemento.

lista_carros = list(tupla_carros) # fazendo um cast para transformar o tipo de dado de tupla para lista.

lista_carros[1] = "Focus" # mudar o carro na posição 2 para Focus.

tupla_carros = tuple(lista_carros) # transformando para uma tupla.

for x in tupla_carros:
    print(x)
