import time
class Carro: #Mi Clase Principal
    def __init__(self, Marca, Modelo, Precio):# metodo constructor de mi clase
        self.Marca = Marca
        self.Modelo = Modelo
        self.Precio = Precio
        self.tuneado = None

    def Encender(self):
        print("Encendiendo...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Brum burm brrrrrrr...")
        time.sleep(2)

    def Acelerar(self):
        n = 0
        print("Acelerando...")
        time.sleep(2)
        while n <= 300:
            print("Velocidad...", n, "Km", "=͟͟͞͞(꒪ᗜ ꒪‧̣̥̇)")
            n += 50
            time.sleep(1)

    def Frenar(self):
        print("=͟͟͞͞(꒪ᗜ꒪‧̣̥̇)Frenando....")
        time.sleep(1)
        print("Σ(ﾟ口ﾟ;)//")
        time.sleep(1)
        print("૮₍ ˃ ⤙ ˂ ₎ა=͟͟͞͞(=͟͟͞͞(")
        time.sleep(1)
        print("Frenado (๑>؂•̀๑)")
        time.sleep(1)

    def Describir(self):
        print("Carro Marca:", self.Marca)
        print("Soy de Modelo:", self.Modelo)
        if self.tuneado:
            print("Carro tuneado")
        else:
            print("No tiene tuneado")

    def Poner_tuneada(self, tuneado):
        self.tuneado = tuneado

    def Donitas(self, material):
        print("Está quemando la llanta de:", material)

class Dueño:
    def __init__(self, nombre):# metodo constructor de mi clase
        self.nombre = nombre
        self.carros = []

    def Comprar_carro(self, carro):
        self.carros.append(carro)
        print("Acabas de comprar:", carro.Marca)
        time.sleep(2)
        print("Comprado")

    def Listar_carros(self):
        print(self.nombre, "tiene los siguientes carros:")
        for carro in self.carros:
            print(carro.Marca)

    def Usar_Carro(self):
        print(self.nombre, "está paseando en coche")
        for carro in self.carros:
            carro.Encender()
            carro.Acelerar()

class Mecanico:
    def __init__(self, nombre):# metodo constructor de mi clase
        self.nombre = nombre
        self.carros_arreglados = []

    def Reparar_carro(self, carro):
        self.carros_arreglados.append(carro)
        print(self.nombre, "está arreglando el carro:", carro.Marca)

    def Listar_carros_arreglados(self):
        print(self.nombre, "ha arreglado los siguientes carros:")
        for carro in self.carros_arreglados:
            print(carro.Marca)

class Tuneado:
    def __init__(self, color, material):# metodo constructor de mi clase
        self.color = color
        self.material = material

    def Describir(self):
        print("Este de color", self.color, "y material", self.material)

class Carro_competitivo(Carro):# metodo constructor de mi clase
    def __init__(self, Marca, Modelo, Precio, Tipo_carrera):
        super().__init__(Marca, Modelo, Precio)
        self.Tipo_carrera = Tipo_carrera

    def Carrera(self):
        print(self.Marca, "está en la carrera", self.Tipo_carrera)
        print("Corriendo...")
        print("...")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Kuchao =͟͟͞͞(꒪ᗜ꒪‧̣̥̇)")

    def Describir(self):
        super().Describir()
        print("Soy de carrera:", self.Tipo_carrera)

class Carro_Familiar(Carro):# metodo constructor de mi clase
    def __init__(self, Marca, Modelo, Precio, Tipo_carro):
        super().__init__(Marca, Modelo, Precio)
        self.Tipo_carro = Tipo_carro

    def Describir(self):
        super().Describir()
        print("Soy un automóvil tipo:", self.Tipo_carro)

class Derrapar:
    def __init__(self, material):
        self.material = material
    def Donitas(self, material):
        print("Está quemando la llanta de:", material.material)

class menu():
    dueño_actual = None
    carro_actual = None
    mecanico_actual = None

    while True:
        print("------- Menu Principal ----------")
        print(" ☆✧˖°⋆.˚   1. Dueño  ☆✧˖°⋆.˚   ")
        print("")
        print(" ☆✧˖°⋆.˚   2. Carros  ☆✧˖°⋆.˚   ")
        print("")
        print(" ☆✧˖°⋆.˚   3. Mecánico  ☆✧˖°⋆.˚   ")
        print("")
        print("  ☆✧˖°⋆.˚  4. Salir  ☆✧˖°⋆.˚   ")
        print("--------------------------------")
        opcion = input("Selecciona una opción: ")
        time.sleep(1)

        if opcion == "1":
            while True:
                print("---------- Menu Dueño ---------")
                print("1. Registrar Dueño")
                print("     (｡- .•)  ")
                print("2. Comprar Carro")
                print("    (=^ ◡ ^=) ")
                print("3. Listar Carros")
                print("   ( ˶ˆ꒳ˆ˵ )  ")
                print("4. Usar Carro")
                print("   ٩(ˊᗜˋ*)و ")
                print("5. Volver al Menú Principal")
                print("------------------------------")
                time.sleep(1)
                opcion_dueño = input("Selecciona una opción: ")

                if opcion_dueño == "1":
                    nombre = input("Introduce el nombre del dueño: ")
                    dueño_actual = Dueño(nombre)
                    print(f"Dueño {nombre} registrado.")
                elif opcion_dueño == "2":
                    if dueño_actual:
                        print("--- Selección de Carro ---")
                        print("     ō͡≡o˞̶  ō͡≡o˞̶   (｡- .•) ")
                        print("Carros deportivos")
                        print("   ( ˶ˆ꒳ˆ˵ )")
                        print("1. Ferrari")
                        print("2. Corvet")
                        print("3. Mustang")
                        print("")
                        print("Carros Familiares")
                        print("   ( ˶ˆ꒳ˆ˵ )")
                        print("4. KIA")
                        print("5. Chevrolet")
                        print("6. Nissan")
                        print("----------------------------")

                        opcion_carro = input("Selecciona un carro para comprar: ")
                        time.sleep(1)
                        if opcion_carro == "1":
                            carro_actual = Carro_competitivo("Ferrari", "A2", 12000,"Formula1")
                        elif opcion_carro == "2":
                            carro_actual = Carro_competitivo("Corvet", "S10", 3300,"Formula1")
                        elif opcion_carro == "3":
                            carro_actual = Carro_competitivo("Mustang", "C23", 7800,"Formula1")
                        elif opcion_carro == "4":
                            carro_actual = Carro_Familiar("kia", "A3", 3300,"Carro familiar")
                        elif opcion_carro == "5":
                            carro_actual = Carro_Familiar("Chevrolet", "PRO3", 7800,"Carro familiar")
                        elif opcion_carro == "6":
                            carro_actual = Carro_Familiar("Nissan", "B12", 3300,"Carro familiar")

                        dueño_actual.Comprar_carro(carro_actual)
                    else:
                        print("Primero debes registrar un dueño.")
                elif opcion_dueño == "3":
                    if dueño_actual:
                        dueño_actual.Listar_carros()
                    else:
                        print("Primero debes registrar un dueño.")
                elif opcion_dueño == "4":
                    if dueño_actual:
                        dueño_actual.Usar_Carro()
                    else:
                        print("Primero debes registrar un dueño.")
                elif opcion_dueño == "5":
                    break

        elif opcion == "2":
            while True:
                print("------ Menú Carros ------")
                print("ō͡≡o˞̶  ō͡≡o˞̶  ō͡≡o˞̶  ō͡≡o˞̶   ō͡≡o˞̶")
                print("1. Encender")
                print("2. Acelerar")
                print("3. Frenar")
                print("4. Describir")
                print("5. Poner Tuneado")
                print("6. Carrera")
                print("7. Derrapar")
                print("8. Volver al Menú Principal")
                print("ō͡≡o˞̶  ō͡≡o˞̶  ō͡≡o˞̶  ō͡≡o˞̶   ō͡≡o˞̶")
                print("------------------------------")
                time.sleep(1)

                opcion_carro = input("Selecciona una opción: ")

                if opcion_carro == "1":
                    if carro_actual:
                        carro_actual.Encender()
                    else:
                        print("Primero debes seleccionar un carro.")
                elif opcion_carro == "2":
                    if carro_actual:
                        carro_actual.Acelerar()
                    else:
                        print("Primero debes seleccionar un carro.")
                elif opcion_carro == "3":
                    if carro_actual:
                        carro_actual.Frenar()
                    else:
                        print("Primero debes seleccionar un carro.")
                elif opcion_carro == "4":
                    if carro_actual:
                        carro_actual.Describir()
                    else:
                        print("Primero debes seleccionar un carro.")
                elif opcion_carro == "5":
                    if carro_actual:
                        color = input("Introduce el color del tuneado: ")
                        material = input("Introduce el material del tuneado: ")
                        tuneado = Tuneado(color, material)
                        carro_actual.Poner_tuneada(tuneado)
                    else:
                        print("Primero debes seleccionar un carro.")
                elif opcion_carro == "6":
                    if carro_actual:
                        carro_actual.Carrera()
                    else:
                        print("Primero debes seleccionar un carro Deportivo")
                elif opcion_carro == "7":
                    carro_actual.Donitas(material)
                elif opcion_carro == "8":
                    break
                

        elif opcion == "3":
            while True:
                print("--- Menú Mecánico ---")
                print("1. Registrar Mecánico")
                print("2. Reparar Carro")
                print("3. Listar Carros Arreglados")
                print("4. Volver al Menú Principal")
                print("------------------------------")
                time.sleep(1)

                opcion_mecanico = input("Selecciona una opción: ")

                if opcion_mecanico == "1":
                    nombre = input("Introduce el nombre del mecánico: ")
                    mecanico_actual = Mecanico(nombre)
                    print(f"Mecánico {nombre} registrado.")
                elif opcion_mecanico == "2":
                    if mecanico_actual:
                        print("---- Selección de Carro ----")
                        print("     ō͡≡o˞̶  ō͡≡o˞̶   (｡- .•) ")
                        print("   ( ˶ˆ꒳ˆ˵ )")
                        print("1. Ferrari")
                        print("2. Corvet")
                        print("3. Mustang")
                        print("   ( ˶ˆ꒳ˆ˵ )")
                        print("4. KIA")
                        print("5. Chevrolet")
                        print("6. Nissan")
                        print("     ō͡≡o˞̶  ō͡≡o˞̶   (｡- .•) ")
                        print("------------------------------")

                        opcion_carro = input("Selecciona un carro para reparar: ")

                        if opcion_carro == "1":
                            carro_actual = Carro_competitivo("Ferrari", "A2", 12000,"Formula1")
                        elif opcion_carro == "2":
                            carro_actual = Carro_competitivo("Corvet", "S10", 3300,"Formula1")
                        elif opcion_carro == "3":
                            carro_actual = Carro_competitivo("Mustang", "C23", 7800,"Formula1")
                        elif opcion_carro == "4":
                            carro_actual = Carro_Familiar("kia", "A3", 3300)
                        elif opcion_carro == "5":
                            carro_actual = Carro_Familiar("Chevrolet", "PRO3", 7800)
                        elif opcion_carro == "6":
                            carro_actual = Carro_Familiar("Nissan", "B12", 3300)
                        mecanico_actual.Reparar_carro(carro_actual)
                    else:
                        print("Primero debes registrar un mecánico.")
                elif opcion_mecanico == "3":
                    if mecanico_actual:
                        mecanico_actual.Listar_carros_arreglados()
                    else:
                        print("Primero debes registrar un mecánico.")
                elif opcion_mecanico == "4":
                    break
                
        elif opcion == "4":
            print("Saliendo...(｡- .•)y")
            break
        

menu()
#commit-“Examen Parcial 2”