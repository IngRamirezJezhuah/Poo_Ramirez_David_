import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
)
cursor = connection.cursor()

class Cliente():
    def __init__(self) -> None:
        self.tabla = "Cliente"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        nombreCliente = input("ingresa el nombre del cliente: ")
        curp = input("ingrese la curp del cliente: ")
        telefono = input("ingrese el telefono del cliente: ")
        correo = input("Ingrese el correo electronico: ")
        Facutracion = input("ingrese el folio de facturacion: ")
        query = "INSERT INTO cliente (Nombre,Curp,Telefono,Correo,Facturacion) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (nombreCliente,curp,telefono,correo,Facutracion))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            nombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Curp del Cliente: {resultados[0][3]}")
            curp = input("Ingrese la curp: ")

            print(f"Teléfono del Cliente: {resultados[0][2]}")
            telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (nombreCliente,curp,telefono,correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del Cliente {fila[0]}")
                print(f"Nombre del cliente: {fila[1]}")
                print(f"Curp del cliente: {fila[2]}")
                print(f"Telefono del cliente: {fila[3]}")
                print(f"Correo del cliente: {fila[4]}")
                print(f"No. folio: {fila[5]}")
                print("--------------------------------------------------------")
        else:
            print("no se encontraron datos disponibles")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

#///////////////////////////////////////////////////////////////////////////////
class Compra():
    def __init__(self) -> None:
        self.tabla = "Compras"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        producto_id = int(input("Ingrese el ID del producto: "))
        cliente_id = int(input("Ingrese el ID del cliente: "))
        fecha = input("Ingresa la fecha de compra (YYYY-MM-DD): ")
        factura = input("Ingrese el número de factura: ")
        total = input("Ingrese el total de la compra: ")
        
        # Consulta SQL para insertar en la tabla compra
        query = "INSERT INTO compra (Producto_id, Cliente_id, Fecha, Factura, Total) VALUES (%s, %s, %s, %s, %s)"
        
        try:
            cursor.execute(query, (producto_id, cliente_id, fecha, factura, total))
            connection.commit()
            print("Compra registrada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")



    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id de la compra a borrar: ")
        borrar = f"DELETE FROM compra WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"Id del producto: {resultados[0][0]}")
            print(f"id del Cliente: {resultados[0][2]}")

            print(f"Fecha de compra: {resultados[0][3]}")
            fecha = input("ingresa la fecha de compra: ")

            print(f"no de factura: {resultados[0][4]}")
            factura = input("ingrese el numero de Factura: ")

            print(f"Total de la compra: {resultados[0][5]}")
            total = input("Ingrese el total de la compra: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (fecha,factura,total , id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM compra")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"Id del producto: {Mostrar[0]}")
                print(f"id del Cliente: {Mostrar[2]}")
                print(f"Fecha de compra: {Mostrar[3]}")
                print(f"No. de factura: {Mostrar[4]}")
                print(f"Total de la compra: {Mostrar[5]}")
                print("--------------------------------------------------------")
        else:
            print("No se encontraron datos disponibles")
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

#///////////////////////////////////////////////////////////////////////////////
class Empleados():
    def __init__(self) -> None:
        self.tabla = "Empleados"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")


#///////////////////////////////////////////////////////////////////////////////
class Gerente():
    def __init__(self) -> None:
        self.tabla = "Gerente"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

#///////////////////////////////////////////////////////////////////////////////
class Producto():
    def __init__(self) -> None:
        self.tabla = "Producto"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

#///////////////////////////////////////////////////////////////////////////////
class Provee():
    def __init__(self) -> None:
        self.tabla = "Provee"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")
    
#///////////////////////////////////////////////////////////////////////////////
class Provedor():
    def __init__(self) -> None:
        self.tabla = "Provedor"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

#///////////////////////////////////////////////////////////////////////////////
class Tienda():
    def __init__(self) -> None:
        self.tabla = "Tienda"

    def secuencia_menu(self):
        while True:
            x = tienda.menu()
            match x:
                case "1":
                    self.registrar()
                case "2":
                    self.consultar()
                case "3":
                    self.editar()
                case "4":
                    self.borrar()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):
        print("_________________________________________")
        print(f"|{self.tabla.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Consultar                            |")
        print("|3)Editar                               |")
        print("|4)Borrar                               |")
        print("|5)Salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        NombreCliente = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Correo = input("Ingrese el correo electronico: ")
        query = "INSERT INTO cliente (Nombre,Telefono,Correo) VALUES (%s,%s,%s)"
        cursor.execute(query, (NombreCliente,Telefono,Correo))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del cliente a borrar: ")
        borrar = f"DELETE FROM cliente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del cliente: {resultados[0][0]}")
            print(f"Nombre del Cliente: {resultados[0][1]}")
            NombreCliente = input("Ingresa el nombre del cliente: ")
            
            print(f"Teléfono del Cliente: {resultados[0][2]}")
            Telefono = input("Ingresa el teléfono del cliente: ")
            
            print(f"Correo del Cliente: {resultados[0][3]}")
            Correo = input("Ingresa el correo electrónico: ")
            
            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (NombreCliente, Telefono, Correo, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM cliente")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Cliente {fila[0]}")
            print(f"Nombre del cliente: {fila[1]}")
            print(f"Telefono del cliente: {fila[2]}")
            print(f"Correo del cliente: {fila[3]}")
            print("--------------------------------------------------------")
    
    def producto(self):  
        cliente.consultar()
        id = input("Ingrese el id del cliente a consultar: ")
        cursor.execute("SELECT * FROM cliente WHERE id=%s",(id,))
        Mostrar = cursor.fetchone()
        if Mostrar:
            print("Datos de cliente")
            print(f"id del cliente: {Mostrar[0]}")
            print(f"Nombre del cliente: {Mostrar[1]}")
            print(f"Numero del cliente: {Mostrar[2]}")
            print(f"Correo del cliente: {Mostrar[3]}")
            print("-----------------")
            print(f"Datos del Producto comprado:")
            cursor.execute("SELECT * FROM productos WHERE id_cliente=%s",(Mostrar[0],))
            resultados = cursor.fetchall()
            if resultados:
                for fila in resultados:
                    print(f"id dels Producto: {fila[0]}")
                    print(f"Tipo de Producto: {fila[1]}")
                    print(f"Marca: {fila[2]}")
            else:
                print("No se encontraron resultados")
        else:
            print("No se encontro ningun producto en la tineda con el id proporcionado.")
            print("---------")
            print("--------------------------------------------------------")

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
    print("|1) Cliente                             |")
    print("|2) Comprar                             |")
    print("|3) Empleados                           |")
    print("|4) Gerente                             |")
    print("|5) Productros                          |")
    print("|6) Provee                              |")
    print("|7) Provedor                            |")
    print("|8) Tienda                              |")
    print("|9)Salir                                |")
    print("_________________________________________")
    x = input("¿Cual opcion deseas escojer?")
    match x:
        case "1":
            cliente.secuencia_menu()
        case "2":
            compra.secuencia_menu()
        case "3":
            empleados.secuencia_menu()
        case "4":
            gerente.secuencia_menu()
        case "5":
            produco.secuencia_menu()
        case "6":
            provee.secuencia_menu()
        case "7":
            provedor.secuencia_menu()
        case "8":
            tienda.secuencia_menu()
        case "9":
            break
        case _:
            print("Favor de escribir una opcion valida")

###################################################################################

if connection.is_connected():
    connection.close()
    print("Conexión cerrada")
    print("Adios bye bye ૮₍´｡ᵔ ꈊ ᵔ｡`₎ა ")