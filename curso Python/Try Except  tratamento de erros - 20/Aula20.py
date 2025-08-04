# O comando "Try", é um comando para tratamento de erros, ele permite verificar o bloco
# e se esse bloco contiver algum erro, gera uma "Except" e executa a rotina do execpt.
# Existe o bloco "finally" que executa idependente do erro ou não.


# PARTE 1----------------------------------------------------------------------
try:
    print(x)

except NameError: # Para except's conhecidos.
    print("X não definido")

except:
    print("Erro desconhecido")

print("\n")
    
# PARTE 2----------------------------------------------------------------------

y = 10

try:
    print(y)

except:
    print("Erro no programa")

else: # Caso não dê erro no except
    print("Tudo certo")

finally:
    print("Fim do tratamento")

print("\n")

# PARTE 3----------------------------------------------------------------------

# Disparo de uma exeção que não permita tipos de valores.

#z = -10
t = 10

#if z < 1: 
    # gerando uma exeção. Para a execução do programa e emite uma mensagem mais amigável.
#    raise Exception("Valor não permitido") 

if not type(t) is int: # Se não for do tipo inteiro.
    raise Exception("Somente números")
else :
    print(t)
