carros = ["HRV", "Golf", "Argo", "Focus"] # Atribuindo ao carros um list

carros.append("Fit") # Adicionando informações na lista "carros"
carros.append("Fusion")
carros.append("Polo")

# carros.pop() vai remover a última informação da lista
# carros.clear() Remove todas as informações da lista
# carros2 = list(carros) copiando uma lista para outra

carros3 = ["Fusca", "147", "Brasilia", "Celta"]
carros4 = carros3 + carros # concatenando listas

print(str(len(carros)) + " carros na lista") # Trasnformando todas as informações da lista em string e contando

print(carros4)