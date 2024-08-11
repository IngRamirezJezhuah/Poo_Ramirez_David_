class Perro:
    def __init__(self,nombre,raza,edad):#este es el metodo constructor que es donde damos nuestros atributos en si parametros, init es mi constructor
        self.nombre = nombre #es el self para jalar los metodos o los atributos que tiene nuestra clase
        self.raza = raza#atributo 
        self.edad = edad#atributo}
        self.collar = None
    #aca pues definimos las acciones que vamos a hacer mis metodos normales o funciones
    def Ladrar(self):
        print("woof ૮ • ﻌ • ა")

    def Comer(self):
        print("comiendo ...")

    def Describir(self):
        print("soy un perro llamado:",self.nombre)
        print("Soy de raza:",self.raza)
        print("Tengo:",self.edad,"añitos")
        #se define mi 
        if self.collar:
            print("llevo puesto collar de color",
                self.collar.color,"y material", self.collar.material)
        else:
            print("no tiene collar")
    def Poner_collar(self,collar):
        self.collar = collar
#esta ya es una dependecnia, ho se debe que hacer el atributo, esta solo se pude usar si se toma
    def Jugar(self,juguete):
        print(self.nombre,"esta jugando con",juguete.nombre)

class Dueño:
    def __init__(self,nombre):
        self.nombre = nombre
        self.perros = []
    def Añadir_Perro(self,perro):
        self.perros.append(perro)
        print(perro.nombre, "añadido a la lista de perros de", self.nombre)   
    def Listar_Perro(self):
        print(self.nombre,"tiene los siguientes Perros:")
        for perro in self.perros:
            print("૮ • ﻌ • ა",perro.nombre)
    def Pasear_Perros(self):
        print(self.nombre,"esta paseando a sus perros: ")
        for perro in self.perros:
            perro.Ladrar()

Perro1 = Perro("Firulais","Chiuahua",3,)
Perro2 = Perro("Max","Pitbull",5)

print("El nombre de mi perro es:",Perro1.nombre)
print("La edad de mi perro:",Perro2.edad)
print("Mi perro 2 es:",Perro2.nombre, Perro2.edad)

print(Perro1.nombre,"ladra")
print(Perro1.nombre,":")
Perro1.Ladrar()
print(Perro2.nombre,"Come")
Perro2.Comer()

dueño = Dueño("DJ")

dueño.Añadir_Perro(Perro1)
dueño.Añadir_Perro(Perro2)
dueño.Listar_Perro()
dueño.Pasear_Perros()