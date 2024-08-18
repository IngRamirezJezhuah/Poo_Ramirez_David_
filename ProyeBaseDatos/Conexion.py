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
            
            comando = "UPDATE cliente SET Nombre = %s, Curp = %s, Telefono = %s, Correo = %s, facturacion = %s WHERE id = %s"
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
        producto.consultar()
        datos = cursor.fetchall
        if datos:
            producto_id = int(input("Ingrese el ID del producto: "))
            cliente_id = int(input("Ingrese el ID del cliente: "))
        else:
            print("no hay datos registrados")

        fecha = input("Ingresa la fecha de compra (YYYY-MM-DD): ")
        factura = input("Ingrese el número de factura: ")
        total = input("Ingrese el total de la compra: ")
        
        # Consulta SQL para insertar en la tabla compra
        query = "INSERT INTO compra (Producto_id, Cliente_id, Fecha, Factura, Total) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(query, (producto_id, cliente_id, fecha, factura, total))
        connection.commit()
        print("Compra registrada exitosamente.")
        



    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id de la compra a borrar: ")
        borrar = f"DELETE FROM compra WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
    

    def editar(self):
        compra.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"Id del producto: {resultados[0][0]}")
            id_producto = input("ingrese el numero de Factura: ")

            print(f"id del Cliente: {resultados[0][1]}")
            id_cliente = input("ingrese el numero de Factura: ")

            print(f"Fecha de compra: {resultados[0][2]}")
            fecha = input("ingresa la fecha de compra: ")

            print(f"no de factura: {resultados[0][3]}")
            factura = input("ingrese el numero de Factura: ")

            print(f"Total de la compra: {resultados[0][4]}")
            total = input("Ingrese el total de la compra: ")
            
            comando = "UPDATE compra SET Fecha = %s, Facutra = %s, Total = %s WHERE id = %s"
            cursor.execute(comando, (fecha,factura,total,id_cliente,id_producto , id))
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
                print(f"Id del producto: {Mostrar[0][0]}")
                print(f"id del Cliente: {Mostrar[0][1]}")
                print(f"Fecha de compra: {Mostrar[0][2]}")
                print(f"No. de factura: {Mostrar[0][3]}")
                print(f"Total de la compra: {Mostrar[0][4]}")
                print("--------------------------------------------------------")
        else:
            print("No se encontraron datos disponibles")


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
        Nombreemple = input("ingresa el nombre del usuario: ")
        Telefono = input("ingrese el telefono del usuario: ")
        Curp = input("Ingrese la curp: ")
        Cargo = input("Ingrese el cargo: ")
        fech_contra = input("Ingrese la fecha de contratacion: ")
        tienda.consultar()
        datos = cursor.fetchall
        if  datos:
            id_tienda = input("Ingrese el id de la tineda donde trabaja:")
        else:
            print("no hay tienda registradas")
        query = "INSERT INTO empleados (Nombre,Telefono,Curp,Cargo,fech_contrat,id_tienda) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (Nombreemple,Telefono,Curp,Cargo,fech_contra,id_tienda))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del empleado a borrar: ")
        borrar = f"DELETE FROM empleados WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
        

    def editar(self):
        empleados.consultar()
        id = input("Ingrese el ID del empleados a editar: ")
        cursor.execute("SELECT * FROM empleados WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del empleado: {resultados[0][0]}")
            print(f"Nombre del empleado: {resultados[0][1]}")
            Nombreemple = input("ingresa el nombre del usuario: ")

            print(f"Nombre del Cliente: {resultados[0][2]}")
            Telefono = input("ingrese el telefono del usuario: ")

            print(f"Nombre del Cliente: {resultados[0][3]}")
            Curp = input("Ingrese el correo electronico: ")

            print(f"Nombre del Cliente: {resultados[0][4]}")
            Cargo = input("Ingrese el correo electronico: ")

            print(f"Nombre del Cliente: {resultados[0][5]}")
            fech_contra = input("Ingrese el correo electronico: ")

            print(f"Nombre del Cliente: {resultados[0][6]}")
            id_tienda = input("Ingrese el id de la tineda donde trabaja")
            
            comando = "UPDATE empleados SET Nombre = %s, Telefono = %s, Curp = %s, Cargo = %s, fech_contra = %s, id_tienda = %s WHERE id = %s"
            cursor.execute(comando, (Nombreemple, Telefono, Curp,Cargo, fech_contra ,id_tienda , id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
        cursor.execute("SELECT * FROM empleados")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del Cliente {fila[0]}")
                print(f"Nombre del cliente: {fila[1]}")
                print(f"Telefono del cliente: {fila[2]}")
                print(f"Correo del cliente: {fila[3]}")
                print("--------------------------------------------------------")
        else:
            print("No se encontraron datos disponibles")


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
        Nombre = input("ingresa el nombre del usuario: ")
        edad = input("ingrese la edad del gerente: ")
        curp = input("Ingrese la curp: ")
        telefono = input("Ingrese el telefono: ")
        fech_asig = input("Ingrese la fecha de asigancion: ")
        tienda.consultar()
        datos = cursor.fetchall
        if  datos:
            id_tienda = input("Ingrese el id de la tineda donde trabaja:")
        else:
            print("no hay tienda registradas")
        query = "INSERT INTO  gerente Nombre, Edad, Curp, Telefono, Fech_asig, id_tienda) VALUES  (%s,%s,%s%s,%s,%s)"
        cursor.execute(query, (Nombre,edad,curp,telefono,fech_asig,id_tienda))
        connection.commit()
        print("Cliente Registrado")

    def borrar(self):
        cliente.consultar()
        id = input("ingrese el id del gerente a borrar: ")
        borrar = f"DELETE FROM gerente WHERE id = {id}"
        cursor.execute(borrar)
        connection.commit()
        print("Cliente eliminado exitosamente")
        

    def editar(self):
        cliente.consultar()
        id = input("Ingrese el ID del cliente a editar: ")
        cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
        resultados = cursor.fetchall()
        if resultados:  # Verificar si se encontró un cliente con ese ID
            print(f"ID del gerente: {resultados[0][0]}")
            print(f"Nombre del Gerente: {resultados[0][1]}")
            Nombre = input("ingresa el nombre del gerente: ")

            print(f"Edad del gerente: {resultados[0][2]}")
            edad = input("ingrese la edad del gerente: ")

            print(f"Curp del gerente: {resultados[0][3]}")
            curp = input("Ingrese la curp: ")

            print(f"Telefono del gerente: {resultados[0][4]}")
            telefono = input("Ingrese el telefono: ")

            print(f"fecha de asignacion del gerente: {resultados[0][5]}")
            fech_asig = input("Ingrese la fecha de asigancion: ")

            print(f"Tienda donde trabaja: {resultados[0][6]}")
            id_tienda = input("Ingrese el id de la tineda donde trabaja:")

            comando = "UPDATE cliente SET Nombre = %s, Telefono = %s, Correo = %s WHERE id = %s"
            cursor.execute(comando, (Nombre,edad,curp,telefono,fech_asig,id_tienda, id))
            connection.commit()
            
            print("Actualización exitosa")
        else:
            print("No se encontró un cliente con ese ID.")
        
        print("-------------------------------------------------------")


    def consultar(self):
            cursor.execute("SELECT * FROM gerente")
            Mostrar = cursor.fetchall()
            print("--------------------------------------------------------")
            for fila in Mostrar:
                print(f"ID del gerente: {Mostrar[0][0]}")
                print(f"Nombre del Gerente: {Mostrar[0][1]}")
                print(f"Edad del gerente: {Mostrar[0][2]}")
                print(f"Curp del gerente: {Mostrar[0][3]}")
                print(f"Telefono del gerente: {Mostrar[0][4]}")
                print(f"fecha de asignacion del gerente: {Mostrar[0][5]}")
                print(f"Tienda donde trabaja: {Mostrar[0][6]}")
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
        cursor.execute("SELECT * FROM producto")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id del Producto {fila[0]}")
            print(f"Nombre del producto: {fila[1]}")
            print(f"Tipo de producto: {fila[2]}")
            print(f"Contenido neto: {fila[3]}")
            print(f"Contenido calorico: {fila[4]}")
            print(f"id_tienda: {fila[5]}")
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
        cursor.execute("SELECT * FROM tienda")
        Mostrar = cursor.fetchall()
        print("--------------------------------------------------------")
        for fila in Mostrar:
            print(f"id de la tienda {fila[0]}")
            print(f"Nombre de la tienda: {fila[1]}")
            print(f"Direccion de la tienda: {fila[2]}")
            print(f"Codigo postal: {fila[3]}")
            print(f"telefono: {fila[3]}")
            print(f"fech_funda: {fila[3]}")
            print("--------------------------------------------------------")
    

cliente = Cliente()
compra = Compra()
empleados = Empleados()
gerente = Gerente()
producto = Producto()
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
            producto.secuencia_menu()
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