#commit - programa 24 - Clases y Objetos Agregacion"
import time 
class Carro:
    def __init__(self,Marca,Modelo,Precio):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Precio = Precio
    def Encender(self):# en este lo que hace es tal cual encenderlo
        print("encendiendo...")
        time.sleep(2)#uso la libreria de time para que a la hora de imprimirlo se tarde
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("brum burm brrrrrrr.....")#aqui se supone que ya se encendio
        time.sleep(2)
    def Acelerar(self):#en este cree y simule lo que es acelerar
        n = 0 # este es mi contador
        print("acelerando...")
        time.sleep(2)#igual hago que se tarde en aparecer para dar la ilucion de acelerar
        while n <= 300:#aqui use un ciclo para que se repitiera hasta 300
            print("velocidad...", n,"Km","=͟͟͞͞(꒪ᗜ ꒪‧̣̥̇)")#hasta le agregue un kaomoji que simula la aceleracion
            n += 50
            time.sleep(1)
    def Frenar(self):#aqui lo que hace es edtenerlo
        print("=͟͟͞͞(꒪ᗜ꒪‧̣̥̇)frenando....") #como estas acelerando tienes que frenas
        time.sleep(1)
        print("Σ(ﾟ口ﾟ;)//")#empiexas a frenar
        time.sleep(1)
        print("૮₍ ˃ ⤙ ˂ ₎ა=͟͟͞͞(=͟͟͞͞(")#sientes el golpe de la frenada
        time.sleep(1)
        print("frenado (๑>؂•̀๑)")# frenaste
        time.sleep(1)

class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros = []
    def Comprar_carro(self,carro):
        self.carros.append(carro)
        print("acabas de comprar:",self.carros)
        time.sleep(2)
        print("Comprado")
    def Listar_carros(self):
        print(self.nombre,"tiene los siguientes carros:")
        
        for carro in self.carros:
            print(carro.Marca)
    def Usar_Carro(self):
        print(self.nombre,"esta paseando en coche")
        for carros in self.carros:
            carros.Encender(),
            carros.Acelerar()

class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_arreglados = []

    def reparar_carro(self,carro):
        self.carros_arreglados.append(carro)
        print(self.nombre,"esta arreglando el carro:", carro.Marca)

    def listar_Carros_Arreglados(self):
        print(self.nombre,"ha arreglado los siguientes carros:")
        for carro in self.carros_arreglados:
            print(carro.Marca)

Ferrarri = Carro("Ferrari","A2",12000)
Corvet = Carro("Corvet","S10",3300)
Mustang = Carro("Mustang","c23",7800)

#print("Carro")
#print(Corvet.Marca,"(｡- .•)")
#Corvet.Encender()
#print("----------------------------------")
#print("Carro")
#print(Ferrarri.Marca,"(｡- .•)")
#Ferrarri.Acelerar()
#print("----------------------------------")
#print("Carro",Mustang.Marca,"(｡- .•)")
#Mustang.Frenar()
#print("----------------------------------")
#print("chao chao ૮ • ﻌ - ა ")

dueño = Dueño("Dj")
#dueño.Comprar_carro(Ferrarri)
#dueño.Comprar_carro(Mustang)
#dueño.Listar_carros()
#dueño.Usar_Carro()

mecanico = Mecanico("Mecanico Geova")
mecanico.reparar_carro(Ferrarri)
mecanico.reparar_carro(Corvet)
mecanico.listar_Carros_Arreglados()
