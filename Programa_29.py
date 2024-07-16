#Programa que contenga un menu que llame a diferentes funciones que expliquen que es abstraccion, encapsulacion, herencia y polimofirsmo
#commit "Programa 29 - Principio de la Poo"
#hehe me dio flojera y voy a reutilizar mi codigo para explicarlo

#Abstraccion
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print(f"{self.marca} {self.modelo} está arrancando.")
        

# Uso
mi_carro = Carro("Toyota", "Corolla")
print("este es un ejemplo de Abstraccion")
mi_carro.arrancar()  # Salida: Toyota Corolla está arrancando.


#Encapsulacion
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca       # Propiedad protegida
        self.modelo = modelo    # Propiedad privada

    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo

# Uso
mi_carro = Carro("Toyota", "Corolla")
print("Ejemplo de encapsulacion")
print(mi_carro.get_modelo())  # Salida: Corolla
mi_carro.set_modelo("Camry")
print(mi_carro.get_modelo())  # Salida: Camry

#Herencia
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def arrancar(self):
        print(f"{self.marca} está arrancando.")

class Carro(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def detalles(self):
        print(f"Carro: {self.marca} {self.modelo}")

# Uso
mi_carro = Carro("Toyota", "Corolla")
print("Ejemplo de Herencia")
mi_carro.arrancar()  # Salida: Toyota está arrancando.
mi_carro.detalles()  # Salida: Carro: Toyota Corolla

#polimorfismo
class Vehiculo:
    def arrancar(self):
        print("El vehículo está arrancando.")

class Carro(Vehiculo):
    def arrancar(self):
        print("El carro está arrancando.")

class Moto(Vehiculo):
    def arrancar(self):
        print("La moto está arrancando.")

# Uso
vehiculo = Vehiculo()
carro = Carro()
moto = Moto()

print("Ejemplo de Polimorfismo")
vehiculo.arrancar()  # Salida: El vehículo está arrancando.
carro.arrancar()     # Salida: El carro está arrancando.
moto.arrancar()      # Salida: La moto está arrancando.

