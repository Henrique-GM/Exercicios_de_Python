#PARTE 1----------------------------------------------------------------------------------------
class Carro:
    velocidade_Max = 0
    ligado = False
    cor = ""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velocidade_Max = 200
c1.cor = "Preto"
c1.ligado = False

print("Velcidade Máxima: " + str(c1.velocidade_Max))
print("Cor: " + c1.cor)

estado = "S" if c1.ligado else "N" # Usando if ternáriio para deixar mais amigável o boleano.

print("Ligado: " + estado)

print("\n")

#PARTE 2----------------------------------------------------------------------------------------

class Carro2:
    velocidade_Max = 0
    ligado = False
    cor = ""

# Um método construtor "def __init__()" é uma função que vai ser chamada quando instanciar um objeto na classe
# O comando "self" é uma passagem/referência para a propria classe.

    def __init__(self, velocidade, ligado, cor):    
        self.velocidade_Max = velocidade
        self.ligado = ligado
        self.cor = cor

    def mostrar(self):
        print("Velcidade Máxima: " + str(self.velocidade_Max))
        print("Cor.............: " + self.cor)

        estado = "S" if self.ligado else "N" # Usando if ternáriio para deixar mais amigável o boleano.

        print("Ligado..........: " + estado)
        print("-----------------------------")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if(self.ligado):
            print("Andando")      
        else: 
            print("Carro desligado")

c4 = Carro2(200, False, "Preto")
c5 = Carro2(120, False, "Branco")
c6 = Carro2(350, False, "Vermelho")

c4.mostrar()
c5.mostrar()
c6.mostrar()

c4.ligar()
c4.andar()

print("\n")

#PARTE 3----------------------------------------------------------------------------------------

# Erança é uma classe que herda outra classe. Classes filhos herdarão a classes pai, ou seja, todasas suas caracteristicas.

class NPC: # Classe base, pai, super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca  
        self.municao = municao  
        self.vivo = True
        self.energia = 100

    def info(self):
        print("nome.....: " + self.nome)
        print("Time.....: " + str(self.time))
        print("Forca....: " + str(self.time))
        print("municao..: " + str(self.time))
        print("Vivo.....: " + ("S" if self.vivo else "N"))
        print("Energia..: " + str(self.time))
        print("-------------------------------------------")

# Soldado vai herdar todo o conteudo da classe NPC
class Soldado(NPC):

    # Quando crio um construtor para a classe filho, esse construtor sobreescreve o construtor da classe pai.
    # Os outros dados "forca" e "municao" serão passados não pelo construtor da classe filho, más vão ser passados ao construtor da classe 
    # pai por parametros locais.

    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        
        # Agora preciso chamar o construtor da classe pai, e passar todos esses parâmetros "nome, time, forca e municao"
        # para isso priciso chamar a função "super()" invoca o metodo/classe da classe pai. O construtor da classe pai.

        super().__init__(nome, time, self.forca, self.municao)
    
class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20

        super().__init__(nome, time, self.forca, self.municao)      

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500

        super().__init__(nome, time, self.forca, self.municao)

        # Uma função invocando um construtor da classe pai.
    def informacao(self):
        super().info()

soldado1 = Guarda("Fábio", 1)
soldado2 = Soldado("Tarcísio", 1)
soldado3 = Elite("Vanderson", 1)
soldado4 = Guarda("Cristiano", 2)
soldado5 = Soldado("Bruno", 2)
soldado6 = Elite("Roberto", 2)

soldado1.info()
soldado2.info()
soldado3.info()
soldado4.info()
soldado5.info()
soldado6.informacao()
