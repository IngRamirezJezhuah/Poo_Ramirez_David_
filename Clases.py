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

#ASOCIACION
class Veterinario:
    def __init__(self,nombre):
        self.nombre= nombre
        self.perros_atendidos = []

    def atender_perro(self,perro):
        self.perros_atendidos.append(perro)
        print(self.nombre, "esta atendiendo a :", perro.nombre)
    
    def listar_perros_atendidos(self):
        print(self.nombre,"ha tratado a los siguientes perritos:")
        for perro in self.perros_atendidos:
            print(perro.nombre)

#COMPOSICION
class Collar:
    def __init__(self,color,material):
        self.color = color
        self.material = material
    def describir(self):
        print("este collar de color", 
        self.color,"y material", self.material)
    def Poner_collar(self,collar):
        self.collar = collar
    
#Herencia
class PerroDeServicio(Perro):#para indicar herencia entre parentesis va superclase, y la clase hija es la de fuera
    def __init__(self,nombre,raza,edad, tipo_servicio):
        super().__init__(nombre,raza,edad)#este es solo para llamarlo a la super clase, se usa el coon codigo super
        self.tipo_servicio = tipo_servicio#este es el nuevo atributo de la clase que heredo
        #por esta razon ya no se vuelve a repetir solo lo hereda
    def Trabajar(self):
        print(self.nombre, "esta trabajando como perro ૮ • ﻌ • ა  de Servicio siendo:",
            self.tipo_servicio)#al ser heredado se puede usar el '.' nombre por que, al heredarlo se puede llamar a si mismo
    def Describir(self):
        #se pone super(), y el metodo que queremos jalar
        super().Describir()#lo chido de la herencia es que ya no se tiene que volver a poner el metodo, solo se usa el super y ya lo tienes
        print("Soy un perro de servicio de tipo:",
            self.tipo_servicio,"૮ • ﻌ • ა ")
        
class Juguete:
    def __init__(self,nombre,material):
        self.nombre = nombre
        self.material = material
    def Describir(self):
        print(self.nombre,"esta hecho de",self.material)

#crear los objetos
Perro1 = Perro("Firulais","Chiuahua",3,)
Perro2 = Perro("Max","Pitbull",5)

#print("El nombre de mi perro es:",Perro1.nombre)
#print("La edad de mi perro:",Perro2.edad)
#print("Mi perro 2 es:",Perro2.nombre, Perro2.edad)

#print(Perro1.nombre,"ladra")
#print(Perro1.nombre,":")
#Perro1.Ladrar()
#print(Perro2.nombre,"Come")
#Perro2.Comer()

dueño = Dueño("DJ")

#dueño.Añadir_Perro(Perro1)
#dueño.Añadir_Perro(Perro2)
#dueño.Listar_Perro()
#dueño.Pasear_Perros()

#NUEVO OBJETO VETERINARIO
veterinario = Veterinario("Dr Richie")

#veterinario.atender_perro(Perro1)
#veterinario.atender_perro(Perro2)
#veterinario.listar_perros_atendidos()

#collar1 = Collar("rojo","cuero")
#collar2 = Collar("plateado","acero")
#print("-----------------------------------------")
#print("El nombre de mi perro es:",Perro1.nombre)
#Perro1.Poner_collar(collar1)
#Perro1.Describir()
#print("-----------------------------------------")
#Perro2.Describir()

perro_servicio = PerroDeServicio("Dandy","Labrador", 5, "Guia")
#print("-----------------------------------------")
#perro_servicio.Trabajar()
#perro_servicio.Describir()
#print("-----------------------------------------")

juguete = Juguete("Pelota","plastico")

Perro1.Jugar(juguete)