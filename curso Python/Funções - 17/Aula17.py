numero1 = 20
numero2 = 11

# Parte 1--------------------------------------------------------------------------------------

def somar():
    resposta = numero1 + numero2

    print("A soma de " + str(numero1) + " e " + str(numero2) + " = " + str(resposta))

def subitrair():
    resposta = numero1 - numero2

    print("Subtração de " + str(numero1) + " e " + str(numero2) + " = " + str(resposta))

def multiplicar():
    resposta = numero1 * numero2

    print("Multiplicação de " + str(numero1) + " e " + str(numero2) + " = " + str(resposta))


def calculos():
    somar()
    subitrair()

calculos()

# Parte 2--------------------------------------------------------------------------------------

def textos(*txt): # Um argumento arbitrários é um tipo de argumento que permite que uma função aceite um número de variáveis de argumentos.
    for i in txt:
        print(i)

print("\n")
textos("Python"," argumentos arbitrários")

def somar2(*numeros): # Argumentos arbitrários em números inteiros.
    
    resposta = 0

    for i in numeros:
        resposta += i

    print("Soma = " + str(resposta))

somar2(5, 2, 30) 

print("\n")

valores = [5, 6, 8, 9, 44] # utilizando outros métodos para substituir os argumentos arbitrários.

def somar3(numeros):

    resposta = 0

    for i in numeros:
        resposta += i

    print("Soma = " + str(resposta))

somar3(valores)

# Parte 3--------------------------------------------------------------------------------------

valores2 = [5, 6, 6, 3]

def somar(numeros):
    
    resposta = 0

    for i in numeros:
        resposta += i

    return resposta # sem o return, não poderá retornar um valor se posto em um print por exemplo.

print("\n")

#def lista(numeros): # Uma forma de imprimir um valor de uma lista.
    
#    for i in numeros:
#        print(i)

#lista(valores)



print(str(valores) + " : soma = " + str(somar(valores)))