class Perro:
    def __init__(self,nombre,raza,edad):#este es el metodo constructor que es donde damos nuestros atributos en si parametros, init es mi constructor
        self.nombre = nombre #es el self para jalar los metodos o los atributos que tiene nuestra clase
        self.raza = raza#atributo 
        self.edad = edad#atributo

    #aca pues definimos las acciones que vamos a hacer mis metodos normales o funciones
    def Ladrar(self):
        print("woof")
    def Comer(self):
        print("comiendo ...")

#crear los objetos
perro1 = Perro("Firulais","Chiuahua",3)
perro2 = Perro("Max","Pitbull",5)

print("El nombre de mi objeto 1 es:",perro1.nombre)
print("La edad de mi objeto 2:",perro2.edad)
print("Mi perro 2 es:",perro2.nombre, perro2.edad)

print(perro1.nombre,"ladra")
print(perro1.nombre,":")
perro1.Ladrar()
print(perro2.nombre,"Come")
perro2.Comer()