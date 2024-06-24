#crea un programa que contenga una clase, con al menos 3 atributos y 3 metodos
# luego crea al menos 2 objetos a partir de la clase y usa algunos atributos y metodos
# Documenta tu codigo. commit "programa23 - Clases y Objetos" #/
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

Ferrarri = Carro("Ferrari","A2",12000)
Corvet = Carro("Corvet","S10",3300)
Mustang = Carro("Mustang","c23",7800)

print("Carro")
print(Corvet.Marca,"(｡- .•)")
Corvet.Encender()
print("----------------------------------")
print("Carro")
print(Ferrarri.Marca,"(｡- .•)")
Ferrarri.Acelerar()
print("----------------------------------")
print("Carro",Mustang.Marca,"(｡- .•)")
Mustang.Frenar()
print("----------------------------------")
print("chao chao ૮ • ﻌ - ა ")