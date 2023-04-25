# Segunda opción del menú ubicado en programa principal.
# Se realizan distintas funciones (retirar dinero, depositar dinero, ver saldo actual, pagar servicios, compra/venta de divisas y eliminar usuario)
# Guarda los datos en archivos luego de modificarse.

#Bibliotecas importadas
import comun
import os

#***********************************************************************************************************************

#Variables y constantes
usuarios = {}
CarpetaUsuarios = "UsuariosYPines.txt"

#***********************************************************************************************************************

#Función para ingresar al usuario
def autenticarUsuario(matriz, tiposCambio):
    if matriz == []:
        print("\nNo existen usuarios regitrados.")
    else:
        cedula = ingresarCedula()
        if cedula != "0":
            pin, nombre = ingresarPin(cedula, matriz)
            if pin != "0":
                print(f"\n¡Bienvenido {nombre}!")
                submenu(cedula, pin, tiposCambio, matriz)

#***********************************************************************************************************************

#Función para ingresar al usuario - Cédula
def ingresarCedula():
    intentos = 3
    while intentos > 0:
        cedula = comun.solicitaCedula() # input("Ingrese su cedula: ")
        if cedula == '0':
            intentos -= 1
        else:
            return cedula
    print("\nHa execido el número máximos de intentos.")
    return "0"

#***********************************************************************************************************************

#Función para ingresar al usuario - PIN
def ingresarPin(cedula, matriz):
    intentos = 3
    while intentos > 0:
        pin = input("Ingrese su PIN: ")
        for i in range(len(matriz)):
            if matriz[i][0] == cedula and matriz[i][2] == pin:
                return pin, matriz[i][1]
        intentos -= 1
        print("El PIN ingresado es incorrecto.")
    print("\nHa execido el número máximosde intentos.")
    return "0", ""

#***********************************************************************************************************************

#Función para ingresar al submenú una vez se verificó el usuario
def submenu(cedula, pin, tiposCambio, matriz):
    while True:
        print("\n1. Retirar dinero\n2. Depositar dinero\n3. Ver saldo actual\n4. Pagar servicios\n5. Compra/Venta de Divisas\n6. Eliminar usuario\n7. Salir")
        opcion = input("Ingrese una opcion de acuerdo al valor asignado: ")
        if opcion == "1":
            retirarDinero(cedula)
        elif opcion == "2":
            depositarDinero(cedula)
        elif opcion == "3":
            verSaldo(cedula)
        elif opcion == "4":
            pagarServicio(cedula, tiposCambio)
        elif opcion == "5":
            compraVentaDivisas(cedula, tiposCambio)
        elif opcion == "6":
            eliminarUsuario(cedula, pin, matriz)
            break
        elif opcion == "7":
            break
        else:
            print("\nLa opción ingresada no corresponde a ninguna de las anteriores.")

#***********************************************************************************************************************

#Función para retirar dinero
def retirarDinero(usuario):
    rutaSaldos = os.path.join(f"{usuario}/saldos.txt")

    archivo = open(rutaSaldos, "r")
    lista = archivo.readlines()
    archivo.close()
    saldos = [n.rstrip() for n in lista]

    while True:
        print("\n1. Dolares\n2. Colones\n3. Bitcoins")
        opcion = input("Por favor ingrese la cuenta de la que desea retirar dinero.\nOpción: ")
        if opcion == "1":
            cuentaDolares(saldos, rutaSaldos)
            cuentaDolares(saldos, rutaSaldos)
            cuentaDolares(saldos, rutaSaldos)
            break
        elif opcion == "2":
            cuentaColones(saldos, rutaSaldos)
            cuentaColones(saldos, rutaSaldos)
            cuentaColones(saldos, rutaSaldos)
            break
        elif opcion == "3":
            cuentaBitcoins(saldos, rutaSaldos)
            cuentaBitcoins(saldos, rutaSaldos)
            cuentaBitcoins(saldos, rutaSaldos)
            break
        else:
            print("La opción ingresada no corresponde a ninguna de las anteriores.")

#*********************************************************

#Función para ingresar el monto a retirar en dolares.
def cuentaDolares(saldos, rutaSaldos):
    print("\nCuenta en Dolares")
    print(f"Saldo actual: {saldos[0]}")
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= float(saldos[0]):
        saldos[0] = str(float(saldos[0]) - float(monto))
        archivo = open(rutaSaldos, "w")
        archivo.write(str(saldos[0]))
        archivo.write("\n")
        archivo.write(str(saldos[1]))
        archivo.write("\n")
        archivo.write(str(saldos[2]))
        archivo.close()
        print(f"Retiro exitoso. Saldo actual: {saldos[0]}")
    else:
        print("Saldo insuficiente.")

#*********************************************************

#Función para ingresar el monto a retirar en colones.
def cuentaColones(saldos, rutaSaldos):
    print("\nCuenta en Colones")
    print(f"Saldo actual: {saldos[1]}")
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= float(saldos[1]):
        saldos[0] = str(float(saldos[1]) - float(monto))
        archivo = open(rutaSaldos, "w")
        archivo.write(str(saldos[0]))
        archivo.write("\n")
        archivo.write(str(saldos[1]))
        archivo.write("\n")
        archivo.write(str(saldos[2]))
        archivo.close()
        print(f"Retiro exitoso. Saldo actual: {saldos[1]}")
    else:
        print("Saldo insuficiente.")

#*********************************************************

#Función para ingresar el monto a retirar en bitcoins.
def cuentaBitcoins(saldos, rutaSaldos):
    print("\nCuenta en Bitcoins")
    print(f"Saldo actual: {saldos[2]}")
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= float(saldos[2]):
        saldos[0] = str(float(saldos[2]) - float(monto))
        archivo = open(rutaSaldos, "w")
        archivo.write(str(saldos[0]))
        archivo.write("\n")
        archivo.write(str(saldos[1]))
        archivo.write("\n")
        archivo.write(str(saldos[2]))
        archivo.close()
        print(f"Retiro exitoso. Saldo actual: {saldos[2]}")
    else:
        print("Saldo insuficiente.")

#***********************************************************************************************************************

#Función para depositar dinero
def depositarDinero(usuario):
    rutaSaldos = os.path.join(f"{usuario}/saldos.txt")

    archivo = open(rutaSaldos, "r")
    lista = archivo.readlines()
    archivo.close()
    saldos = [n.rstrip() for n in lista]

    while True:
        print("\n1. Dolares\n2. Colones\n3. Bitcoins")
        opcion = input("Por favor ingrese la cuenta a la que desea hacer el depósito.\nOpción: ")
        if opcion == "1":
            print("Cuenta en Dolares")
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                saldos[0] = str(float(saldos[0]) + monto)
                archivo = open(rutaSaldos, "w")
                archivo.write(str(saldos[0]))
                archivo.write("\n")
                archivo.write(str(saldos[1]))
                archivo.write("\n")
                archivo.write(str(saldos[2]))
                archivo.close()
                print(f"Depósito exitoso. Saldo actual: {saldos[0]}")
                break
            else:
                print("El monto debe ser positivo.")
        elif opcion == "2":
            print("Cuenta en Colones")
            print(f"Saldo actual: {saldos[1]}")
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                saldos[1] = str(float(saldos[1]) + monto)
                archivo = open(rutaSaldos, "w")
                archivo.write(str(saldos[0]))
                archivo.write("\n")
                archivo.write(str(saldos[1]))
                archivo.write("\n")
                archivo.write(str(saldos[2]))
                archivo.close()
                print(f"Depósito exitoso. Saldo actual: {saldos[1]}")
                break
            else:
                print("El monto debe ser positivo.")
        elif opcion == "3":
            print("Cuenta en Bitcoins")
            print(f"Saldo actual: {saldos[2]}")
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                saldos[2] = str(float(saldos[2]) + monto)
                archivo = open(rutaSaldos, "w")
                archivo.write(str(saldos[0]))
                archivo.write("\n")
                archivo.write(str(saldos[1]))
                archivo.write("\n")
                archivo.write(str(saldos[2]))
                archivo.close()
                print(f"Depósito exitoso. Saldo actual: {saldos[2]}")
                break
            else:
                print("El monto debe ser positivo.")
        else:
            print("La opción ingresada no corresponde a ninguna de las anteriores.")

#***********************************************************************************************************************

#Función para ver el saldo del usuario autenticado
def verSaldo(usuario):
    rutaSaldos = os.path.join(f"{usuario}/saldos.txt")

    archivo = open(rutaSaldos, "r")
    lista = archivo.readlines()
    archivo.close()
    saldos = [n.rstrip() for n in lista]
    print("\nSu saldo actual es: ")
    print(f"Dolares: {saldos[0]}")
    print(f"Colones: {saldos[1]}")
    print(f"Bitcoins: {saldos[2]}")

#***********************************************************************************************************************

#Función para pagar los diferentes servios creados al inicio de forma aleatoria
def pagarServicio(usuario, tiposCambio):
    rutaSaldos = os.path.join(f"{usuario}/saldos.txt")
    archivo = open(rutaSaldos, "r")
    lista = archivo.readlines()
    archivo.close()
    saldos = [n.rstrip() for n in lista]

    while True:
        print("\nIngrese el número correspondiente al nombre del servicio a pagar: ")
        print("1.Electricicdad\n2.Agua\n3.Telefonía\n4.Internet\n5.Impuestos\n6.Colegios Profesionales\n7.Tarjeta de crédito\n8.Salir")
        servicio = input("Opción: ")
        if int(servicio)<=7:
            for i in range(int(len(servicio))):
                rutaServicios = os.path.join(f"{usuario}/{servicio}.txt")
                archivo = open(rutaServicios, "r")
                montoServicio = archivo.readlines()
                archivo.close()
                montoYactividad = [n.rstrip() for n in montoServicio]
                if int(montoYactividad[1]) == 1:
                    print("Saldo activo.")
                    print(f"Saldo a pagar: {montoYactividad[2]} colones")
                    while True:
                        print("\nIngrese el número correspondiente a la cuenta que utilizará para hacer el pago: ")
                        print("1.Dólar\n2.Colones\n3.Bitcoins")
                        cuenta = input("Opción: ")
                        if cuenta == "1":
                            montoAPagar = float(montoYactividad[2]) / float(tiposCambio[1])
                            if float(saldos[0]) >= float(montoAPagar):
                                saldos[0] = str(float(saldos[0]) - float(montoAPagar))
                                archivo = open(rutaSaldos, "w")
                                archivo.write(str(saldos[0]))
                                archivo.write("\n")
                                archivo.write(str(saldos[1]))
                                archivo.write("\n")
                                archivo.write(str(saldos[2]))
                                archivo.close()
                                montoYactividad[2] = 0
                                rutaServicios = os.path.join(f"{usuario}/{servicio}.txt")
                                archivo = open(rutaServicios, "w")
                                archivo.write(str(montoYactividad[0]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[1]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[2]))
                                archivo.close()
                                print(f"Pago exitoso.Saldo:{saldos[0]}")
                                break
                            else:
                                print("La cuenta no tiene fondos suficientes.")
                        elif cuenta == "2":
                            if float(saldos[1]) >= float(montoYactividad[2]):
                                saldos[1] = str(float(saldos[1]) - float(montoYactividad[2]))
                                archivo = open(rutaSaldos, "w")
                                archivo.write(str(saldos[0]))
                                archivo.write("\n")
                                archivo.write(str(saldos[1]))
                                archivo.write("\n")
                                archivo.write(str(saldos[2]))
                                archivo.close()
                                montoYactividad[2] = 0
                                rutaServicios = os.path.join(f"{usuario}/{servicio}.txt")
                                archivo = open(rutaServicios, "w")
                                archivo.write(str(montoYactividad[0]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[1]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[2]))
                                archivo.close()
                                print(f"Pago exitoso.Saldo:{saldos[1]}")
                                break
                            else:
                                print("La cuenta no tiene fondos suficientes.")
                        elif cuenta == "3":
                            montoAPagar = float(montoYactividad[2]) / float(tiposCambio[0])
                            if float(saldos[2]) >= float(montoAPagar):
                                saldos[2] = str(float(saldos[2]) - float(montoAPagar))
                                archivo = open(rutaSaldos, "w")
                                archivo.write(str(saldos[0]))
                                archivo.write("\n")
                                archivo.write(str(saldos[1]))
                                archivo.write("\n")
                                archivo.write(str(saldos[2]))
                                archivo.close()
                                montoYactividad[2] = 0
                                rutaServicios = os.path.join(f"{usuario}/{servicio}.txt")
                                archivo = open(rutaServicios, "w")
                                archivo.write(str(montoYactividad[0]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[1]))
                                archivo.write("\n")
                                archivo.write(str(montoYactividad[2]))
                                archivo.close()
                                print(f"Pago exitoso.Saldo:{saldos[2]}")
                                break
                            else:
                                print("La cuenta no tiene fondos suficientes.")
                        else:
                            print("El valor ingresado no corresponde a ninguna de las opciones")
                else:
                    print("Servicio inactivo.")
        else:
            if int(servicio) == 8:
                print("Volviendo al menú.\n")
                break

#***********************************************************************************************************************

#Función para comprar y vender moneda - inicial
def compraVentaDivisas(usuario, tiposCambio):
    rutaSaldos = os.path.join(f"{usuario}/saldos.txt")
    archivo = open(rutaSaldos, "r")
    lista = archivo.readlines()
    archivo.close()
    saldos = [n.rstrip() for n in lista]
    while True:
        print("\nIngrese el número correspondiente a la operación que desea realizar: ")
        print("1.Compra de Colones\n2.Venta de Colones\n3.Compra de Dólares\n4.Venta de Dólares\n5.Compra de Bitcoins\n6.Venta de Bitcoins\n7.Salir")
        opcion = input("Opción: ")
        conversionMonedas(opcion, rutaSaldos, tiposCambio, saldos)
        if opcion == "7":
            break

#***********************************************************************************************************************

#Función para comprar y vender moneda - dividida
def conversionMonedas(opcion, rutaSaldos, tiposCambio, saldos):
    if opcion == "1" or opcion == "2":
#menú de Colones
        while True:
            print("\nIngrese el número correspondiente a la cuenta que desea utilizar para la conversión: ")
            print("1.Dólares\n2.Bitcoins")
            cuenta = input("Opción: ")
#Compra de Colones
            if opcion == "1":
                montoAComprar = float(input("Ingrese el monto en colones que desea comprar: "))
# comprar colones con dólares
                if cuenta == "1":
                    conversionCompra = montoAComprar / float(tiposCambio[7])
                    if conversionCompra <= float(saldos[0]):
                        saldos[0] = str(float(saldos[0]) - float(conversionCompra))
                        saldos[1] = str(float(saldos[1]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Comprar colones con bitcoins
                if cuenta == "2":
                    conversionCompra = montoAComprar / float(tiposCambio[6])
                    if conversionCompra <= float(saldos[2]):
                        saldos[2] = str(float(saldos[2]) - float(conversionCompra))
                        saldos[1] = str(float(saldos[1]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Venta de Colones
            elif opcion == "2":
                montoAVender = float(input("Ingrese el monto en colones que desea vender: "))
# Vender colones con dólares
                if cuenta == "1":
                    conversionVenta = montoAVender / float(tiposCambio[3])
                    if conversionVenta <= float(saldos[1]):
                        saldos[1] = str(float(saldos[1]) - float(conversionVenta))
                        saldos[0] = str(float(saldos[0]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
#Vender colones con bitcoins
                if cuenta == "2":
                    conversionVenta = montoAVender / float(tiposCambio[0])
                    if conversionVenta <= float(saldos[1]):
                        saldos[1] = str(float(saldos[1]) - float(conversionVenta))
                        saldos[2] = str(float(saldos[2]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
#menú de Dólares
    elif opcion == "3" or opcion == "4":
        while True:
            print("\nIngrese el número correspondiente a la cuenta que desea utilizar para la conversión: ")
            print("1.Colones\n2.Bitcoins")
            cuenta = input("Opción: ")
            if opcion == "3":
                montoAComprar = float(input("Ingrese el monto en dólares que desea comprar: "))
#Comprar dolares con colones
                if cuenta == "1":
                    conversionCompra = montoAComprar * float(tiposCambio[10])
                    if conversionCompra <= float(saldos[1]):
                        saldos[1] = str(float(saldos[1]) - float(conversionCompra))
                        saldos[0] = str(float(saldos[0]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Comprar dolares con bitcoins
                if cuenta == "2":
                    conversionCompra = montoAComprar * float(tiposCambio[11])
                    if conversionCompra <= float(saldos[2]):
                        saldos[2] = str(float(saldos[2]) - float(conversionCompra))
                        saldos[0] = str(float(saldos[0]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Vender dólares con colones
            elif opcion == "4":
                montoAVender = float(input("Ingrese el monto en dólares que desea vender: "))
                if cuenta == "1":
                    conversionVenta = montoAVender * float(tiposCambio[4])
                    if conversionVenta <= float(saldos[0]):
                        saldos[0] = str(float(saldos[0]) - float(conversionVenta))
                        saldos[1] = str(float(saldos[1]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
                        # Vender dólares con bitcoins
                if cuenta == "2":
                    conversionVenta = montoAVender * float(tiposCambio[5])
                    if conversionVenta <= float(saldos[0]):
                        saldos[0] = str(float(saldos[0]) - float(conversionVenta))
                        saldos[2] = str(float(saldos[2]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
#menú Bitcoins
    elif opcion == "5" or opcion == "6":
        while True:
            print("\nIngrese el número correspondiente a la cuenta que desea utilizar para la conversión: ")
            print("1.Dólares\n2.Colones")
            cuenta = input("Opción: ")
            if opcion == "5":
                montoAComprar = float(input("Ingrese el monto en bitcoins que desea comprar: "))
# Comprar bitcoins con dolares
                if cuenta == "1":
                    conversionCompra = montoAComprar * float(tiposCambio[9])
                    if conversionCompra <= float(saldos[0]):
                        saldos[0] = str(float(saldos[0]) - float(conversionCompra))
                        saldos[2] = str(float(saldos[2]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Comprar bitcoins con colones
                if cuenta == "2":
                    conversionCompra = montoAComprar * float(tiposCambio[8])
                    if conversionCompra <= float(saldos[1]):
                        saldos[1] = str(float(saldos[1]) - float(conversionCompra))
                        saldos[2] = str(float(saldos[2]) + float(conversionCompra))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La compra se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
            elif opcion == "6":
                montoAVender = float(input("Ingrese el monto en bitcoins que desea vender: "))
# Vender bitcoins con dólares
                if cuenta == "1":
                    conversionVenta = montoAVender * float(tiposCambio[3])
                    if conversionVenta <= float(saldos[2]):
                        saldos[2] = str(float(saldos[2]) - float(conversionVenta))
                        saldos[0] = str(float(saldos[0]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break
# Vender bitcoins con dólares
                if cuenta == "2":
                    conversionVenta = montoAVender * float(tiposCambio[2])
                    if conversionVenta <= float(saldos[2]):
                        saldos[2] = str(float(saldos[2]) - float(conversionVenta))
                        saldos[1] = str(float(saldos[1]) + float(conversionVenta))
                        archivo = open(rutaSaldos, "w")
                        archivo.write(str(saldos[0]))
                        archivo.write("\n")
                        archivo.write(str(saldos[1]))
                        archivo.write("\n")
                        archivo.write(str(saldos[2]))
                        archivo.close()
                        print("La venta se ha realizado con éxito.")
                        break
                    else:
                        print("Saldo insuficiente")
                        break

    elif opcion != "7":
        print("Opción incorrecta.")

#***********************************************************************************************************************

#Función para eliminar el usuario autenticado
def eliminarUsuario(cedula, pin, matriz):
    pinIngresado = input("Ingrese su PIN: ")
    if pin == pinIngresado:
        eliminar = comun.eliminaUsuario(cedula, matriz)
        if eliminar is True:
            archivo = open(comun.NombreArchivoUsuarios, "w")
            for k in range(len(matriz)):
                for j in range(len(matriz[k])):
                    archivo.write(matriz[k][j])
                    archivo.write("\n")
            archivo.close()
        print("Usuario eliminado con éxito.")
    else:
        print("PIN incorrecto.\nVolviendo al menú/")





