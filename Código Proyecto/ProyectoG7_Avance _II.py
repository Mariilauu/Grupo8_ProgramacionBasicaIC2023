#Fecha: 2/4/2023

import os
import getpass
import random

def registrarNuevoUsuarioCedula ():
    # Permitirá almacenar el número de cédula del nuevo usuario.
    intentos = 3
    while intentos>0:
        print("\nSolicitud de número de cédula.")
        cedulaNueva = input("Ingrese el número de cédula, por favor. Nota: Esta no puede ser mayor o menor a 9 dígitos.\nCédula: ")
        if cedulaNueva.isdigit() and len(cedulaNueva)==9:
            #la cedula es repetida? si, otro intento.  No, return cedulaNueva
            break
        else:
            intentos -= 1
            print("Su cédula no cumple con nueve dígitos o ya está registrado.")
            cedulaNueva="0"
    return cedulaNueva
#***********************************************************************************************************************
def registrarNuevoUsuarioNombre ():
    # Solicitud del Nombre.
    print("\nSolicitud del Nombre.")
    nombreDeUsuario = input("Ingrese su nombre completo, por favor.\nNombre: ")
    return nombreDeUsuario
#***********************************************************************************************************************
def registrarNuevoUsuarioPin():
    # Escogencia del PIN
# Falta GETPASS
    while True:
        print("\nEscogencia del PIN.")
        pin = (input("Por favor ingrese un PIN de cuatro dígitos. Este le permitirá ingresar a su cuenta.\nPIN: "))
        if pin.isdigit() and len(pin) == 4:
            while True:
                autentificacionPIN = (input("Reingrese el PIN para su verificación.\nVerificacón PIN: "))
                if autentificacionPIN == pin:
                    break
                else:
                    print("Su PIN de verificación no coincide con el ingresado incialmente.\nPor favor vuelva a intentarlo")
            break
        else:
            print("Su PIN debe contener cuatro dígitos.")
    return autentificacionPIN
#***********************************************************************************************************************
#Registrar Nuevo usuario Depósito Obligatorio
def dolares():
    tipoDecambioDolares = 555.80
    montoMinimoDolares = 100000 / tipoDecambioDolares

    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio>0:
        print("\nPor favor ingrese una cantidad igual o mayor a ", montoMinimoDolares, " dolares.")
        depositoObligatorioDolares = float(input("Depósito: "))
        if depositoObligatorioDolares >= montoMinimoDolares:
            return str(depositoObligatorioDolares)
        else:
            depositoObligatorioDolares ="0"
            print("El monto ingresado es menor al depósito mínimo.")
            intentoDepositoObligatorio -= 1

def colones():
    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio > 0:
        depositoObligatorioColones = float(input("\nPor favor ingrese una cantidad igual o mayor a 100 000 colones.\nDepósito: "))
        if depositoObligatorioColones >= 100000:
            return str(depositoObligatorioColones)
        else:
            depositoObligatorioColones = "0"
            intentoDepositoObligatorio -= 1
            print("El monto ingresado es menor al depósito mínimo.")

def bitcoins():
    tipoDecambioBitcoins = 12418330.72
    montoMinimoBitcoins = 100000 / tipoDecambioBitcoins
    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio > 0:
        print("\nPor favor ingrese una cantidad igual o mayor a ", montoMinimoBitcoins, " bitcoins.")
        depositoObligatorioBitcoins = float(input("Depósito: "))
        if depositoObligatorioBitcoins >= montoMinimoBitcoins:
            return str(depositoObligatorioBitcoins)
        else:
            depositoObligatorioBitcoins ="0"
            intentoDepositoObligatorio -= 1
            print("El monto ingresado es menor al depósito mínimo.")
#***********************************************************************************************************************


#Programa Principal

while True:
    # Menú Principal
    # Presentará las opciones que se pueden realizar en el cajero.
    print("\nBienvenido.\nMenú Principal")
    print("Por favor digite el número de acuerdo a la opción que aparece en pantalla.")
    opcionMenuPrincipal = input("1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: ")
    if opcionMenuPrincipal == "1":
        while True:
            # Registrar Usuario
            # Permitirá almacenar el número de cédula del nuevo usuario.
            cedula = registrarNuevoUsuarioCedula()
            if cedula.isdigit() and len(cedula) == 9:
                print("Su número de cédula ha sido validado.")
            else:
                break
            # Permitirá almacenar el nombre del nuevo usuario.
            nombre = registrarNuevoUsuarioNombre()
            # Permitirá crear un PIN para el nuevo usuario.
            pin = registrarNuevoUsuarioPin()
            if pin.isdigit() and len(pin) == 4:
                print("Su PIN ha sido validado.")
            else:
                break
            # Permitirá hacer un depósito
            print("\nDepósito obligatorio.")
            while True:
                # Selección de la moneda
                print("Ingrese la opción de acuerdo al tipo de moneda que desea utilizar para realizar el depósito.")
                monedaDepositoObligatorio = input("1.Dolares\n2.Colones\n3.Bitcoins\nOpción: ")
                if monedaDepositoObligatorio == "1":
                        monedaDolar = dolares()
                        if monedaDolar == "0":
                            break
                        else:
                            monedaColon = "0"
                            monedaBitcoin = "0"
                        break
                elif monedaDepositoObligatorio == "2":
                        monedaColon = colones()
                        if monedaColon == "0":
                            break
                        else:
                            monedaDolar = "0"
                            monedaBitcoin = "0"
                        break
                elif monedaDepositoObligatorio == "3":
                        monedaBitcoin = bitcoins()
                        if monedaBitcoin == "0":
                            break
                        else:
                            monedaDolar = "0"
                            monedaColon = "0"
                        break
                else:
                    print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")

            archivo = open("Usuarios_y_Pines.txt", 'a')
            archivo.write(cedula)
            archivo.write("\n")
            archivo.write(nombre)
            archivo.write("\n")
            archivo.write(pin)
            archivo.write("\n")
            archivo.close()

            carpetaUsuario = cedula
            if not os.path.exists(carpetaUsuario):
                os.makedirs(carpetaUsuario)
                infoSaldos = "saldos.txt"
                guardarInfoSaldos = os.path.join(carpetaUsuario, infoSaldos)

                archivo = open(guardarInfoSaldos, 'a')
                archivo.write("Dolares\n")
                archivo.write(monedaDolar)
                archivo.write("\nColones\n")
                archivo.write(monedaColon)
                archivo.write("\nBitcoins\n")
                archivo.write(monedaBitcoin)
                archivo.close()



                servicios = "1.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Electricidad\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "2.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Agua\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "3.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Telefonía\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "4.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Internet\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "5.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Impuestos\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "6.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000, 100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Colegios Profesionales\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

                servicios = "7.txt"
                guardarInfoServicios = os.path.join(carpetaUsuario, servicios)
                estadoServicio = random.randint(0, 1)
                montoServicio = random.randint(1000,100000)
                archivo = open(guardarInfoServicios, 'a')
                archivo.write("Tarjeta de Crédito\n")
                archivo.write(str(estadoServicio))
                archivo.write("\n")
                archivo.write(str(montoServicio))
                archivo.close()

            else:
                print("El usuario ", carpetaUsuario," ya existe.")
            break

        # Seleccionar automática y aleatoriamente tres servicios
#Uso de Biblioteca random
        # Guardar la información del nuevo usuario
#Explicación Estructura del Sistema de Archivos
        # Regresar al menú

    elif opcionMenuPrincipal =="2":
        print("op2")
    elif opcionMenuPrincipal =="3":
        print("op3")
    elif opcionMenuPrincipal =="4":
        print("op4")
    elif opcionMenuPrincipal != "1" or opcionMenuPrincipal != "2" or opcionMenuPrincipal != "3" or opcionMenuPrincipal != "4":
        print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
