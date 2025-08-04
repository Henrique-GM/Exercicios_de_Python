# Iterators é um objeto que pde ser iterado, ou seja, pode percorrer valores de uma coleção.

carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Focus", "Onyx", "Fit"]

IteratorsCarros = iter(carros)

while IteratorsCarros:
    
    try:
        print(next(IteratorsCarros)) # Uma função do Iterator para somente avançar na coleção.
    except StopIteration:
        # print("Fim da lista")
        break