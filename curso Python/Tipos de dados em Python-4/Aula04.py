x = 1 # É um INT
x = "Curso" # E uma String
x = 15.6 # E um float
x = True # E um bool

n1 = 5; n2 = 2; x = complex(1j)
x = ["Carro", "Avião", "Navio", 1, 58.3, True] #List / Array "Pode aceitar vários tipos de dados"
x = ("Carro", "Avião", "Navio", 1, 58.3, True) # Tupla "Não aceita substituição de valore já declarados"

x = range(0, 100, 1) #List "uma lista de 0 a 100 de 1 em 1"

x = { # Dict "Trabalha com chave e valor"
    "canal": "CFB cursos",
    "curso": "Curso de Python",
    "nome": "Bruno"
}

x = {5, 7, 4, 5, 7, 4, 8} # Set "Não aceita valor repitido"
x = frozenset({5, 7, 4, 5, 7, 4, 8}) # não se pode mudar os valores"

print("Valor: " + str(x))
print("Tipo: " + str(type(x)))