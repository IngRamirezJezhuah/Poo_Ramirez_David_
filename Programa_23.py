#crea un programa que contenga una clase, con al menos 3 atributos y 3 metodos
# luego crea al menos 2 objetos a partir de la clase y usa algunos atributos y metodos
# Documenta tu codigo. commit "programa23 - Clases y Objetos" #/
import time 
class Carro:
    def __init__(self,Marca,Modelo,Precio):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Precio = Precio
    def Encender(self):
        print("encendiendo...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("brum burm brrrrrrr.....")
        time.sleep(2)
    def Acelerar(self):
        n = 0
        print("acelerando...")
        time.sleep(2)
        while n <= 300:
            print("velocidad...", n,"Km","=͟͟͞͞(꒪ᗜ ꒪‧̣̥̇)")
            n += 50
            time.sleep(1)
    def Frenar(self):
        print("=͟͟͞͞(꒪ᗜ꒪‧̣̥̇)frenando....")
        time.sleep(1)
        print("Σ(ﾟ口ﾟ;)//")
        time.sleep(1)
        print("૮₍ ˃ ⤙ ˂ ₎ა=͟͟͞͞(=͟͟͞͞(")
        time.sleep(1)
        print("frenado (๑>؂•̀๑)")
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