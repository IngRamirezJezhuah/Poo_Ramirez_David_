import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
)
cursor = connection.cursor

class Cliente():
    def __init__(self) -> None:
        self.tabla = "Cliente"
    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")

#///////////////////////////////////////////////////////////////////////////////
class Compra():
    def __init__(self) -> None:
        self.tabla = "Compras"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")

#///////////////////////////////////////////////////////////////////////////////
class Empleados():
    def __init__(self) -> None:
        self.tabla = "Empleados"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")


#///////////////////////////////////////////////////////////////////////////////
class Gerente():
    def __init__(self) -> None:
        self.tabla = "Gerente"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    

#///////////////////////////////////////////////////////////////////////////////
class Producto():
    def __init__(self) -> None:
        self.tabla = "Producto"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    

#///////////////////////////////////////////////////////////////////////////////
class Provee():
    def __init__(self) -> None:
        self.tabla = "Provee"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
#///////////////////////////////////////////////////////////////////////////////
class Provedor():
    def __init__(self) -> None:
        self.tabla = "Provedor"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
#///////////////////////////////////////////////////////////////////////////////
class Tienda():
    def __init__(self) -> None:
        self.tabla = "Tienda"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "a":
                    self.registrar()
                case "b":
                    self.consultar()
                case "c":
                    tienda.editar()
                case "d":
                    self.borrar()
                case "e":
                    self.distribuidor_tienda()
                case "f":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|a)Registrar                            |")
        print("|b)Consultar                            |")
        print("|c)Editar                               |")
        print("|d)Borrar                               |")
        print(f"|e){self.consulta_especial.ljust(37)}|")
        print("|f)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")

cliente = Cliente()
compra = Compra()
empleados = Empleados()
gerente = Gerente()
produco = Producto()
provee = Provee()
provedor = Provedor()
tienda = Tienda()
while True:
    print("_________________________________________")
    print("|         Organizador de tienda         |")
    print("|                                       |")
    print("|Accion a realizar a la tabla:          |")
    print("|                                       |")
    print("|a) Cliente                             |")
    print("|b) Comprar                             |")
    print("|c) Empleados                           |")
    print("|d) Gerente                             |")
    print("|e) Productros                          |")
    print("|f) Provee                              |")
    print("|g) Provedor                            |")
    print("|h) Tienda                              |")
    print("|i)Salir                                |")
    print("_________________________________________")
    x = input("¿Cual opcion deseas escojer?")
    match x:
        case "a":
            cliente.secuencia_menu()
        case "b":
            compra.secuencia_menu()
        case "c":
            empleados.secuencia_menu()
            pass
        case "d":
            gerente.secuencia_menu()
            pass
        case "e":
            produco.secuencia_menu()
        case "f":
            provee.secuencia_menu()
        case "g":
            provedor.secuencia_menu()
        case "h":
            tienda.secuencia_menu()
        case "i":
            break
        case _:
            print("Favor de escribir una opcion valida")

###################################################################################

if connection.is_connected():
    connection.close()
    print("Conexión cerrada")
    print("Adios bye bye ૮₍´｡ᵔ ꈊ ᵔ｡`₎ა ")