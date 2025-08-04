import os
carros = []

class Carro:
    nome = ""
    potencia = 0
    velocidade_Max = 0
    ligado = False


    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velocidade_Max = int(potencia) * 2
        self.ligado = False


    def ligar(self):
        self.ligado = True


    def desligar(self):
        self.ligado = False


    def info(self):
        print("Nome................:" + self.nome)
        print("Potencia............:" + str(self.potencia))
        print("Vel.Máxima..........:" + str(self.velocidade_Max))
        print("Ligado:..:" + ("sim" if self.ligado == True else "não"))   


def Menu():
    os.system("cls") or None # O "or None" é para previnir de algum erro, caso esteja rodando em outro sistema.
    
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print("Quantidade de carros: " + str(len(carros)))

    opcao = input("Digite uma opcao: ")

    return opcao


def NovoCarro():
    os.system("cls") or None
    
    nomeCarro = input("Nome do Carro:.........:")
    potenciaCarro = input("Potência do Carro..:")

    Car = Carro(nomeCarro, potenciaCarro)
    carros.append(Car)
    print("Novo carro criado")

    os.system("pause") # Pausa o processo por um período.


def informacoes():
    os.system("cls") or None
    
    numeroCarro = input("Informe o número do carro que deseja ver as informações: ")

    try:
        carros[int(numeroCarro)].info()
    except:
        print("Carro não existe na lista")
    
    os.system("pause")


def excluirCarro():
    os.system("cls") or None
    
    numeroCarro = input("Informe o número do carro que deseja excluir: ")

    try:
        del carros[int(numeroCarro)]
    except:
        print("Carro não existe na lista")
    
    os.system("pause")


def ligarCarro():
    os.system("cls") or None
    
    numeroCarro = input("Informe o número do carro que deseja ligar: ")

    try:
       carros[int(numeroCarro)].ligar()
       print("Carro ligado")
    except:
        print("Carro não existe na lista")
    
    os.system("pause")


def desligarCarro():
    os.system("cls") or None
    
    numeroCarro = input("Informe o número do carro que deseja ligar: ")

    try:
       carros[int(numeroCarro)].desligar()
       print("Carro desligado")
    except:
        print("Carro não existe na lista")
    
    os.system("pause")


def listarCarros():
    os.system("cls") or None

    posicao = 0

    for i in carros:
        print(str(posicao) + " - " + i.nome)

        posicao = posicao + 1

    os.system("pause")

retorno = Menu() # Retorno do Menu.

while retorno < "7":
    if retorno == '1':
        NovoCarro()
    elif retorno == "2":
        informacoes()
    elif retorno == "3":
        excluirCarro()
    elif retorno == "4":
        ligarCarro()
    elif retorno == "5":
        desligarCarro()
    elif retorno == "6":
        listarCarros()
   
    retorno = Menu()

os.system("cls") or None

print("Programa Finalizado")
