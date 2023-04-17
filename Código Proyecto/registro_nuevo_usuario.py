#Fecha: 2/4/2023

import os
#import getpass
import random

#def agregarUsuariosAMatriz():
 #   archivo = open("Usuarios_y_Pines.txt", "r")
  #  arreglo = archivo.readlines()
   # archivo.close()
    #todoEnUno = [n.rstrip() for n in arreglo]
    #lista = [todoEnUno[i:i + 3] for i in range(0, len(todoEnUno), 3)]


    #matriz = []
    #if len(todoEnUno) > 0:
    #    numeroLinea = 0
    #    totalLineas = len(todoEnUno)
     #   numeroUsuario = totalLineas / 3
      #  for i in range(int(numeroUsuario - 1)):
       #     lista = [todoEnUno[numeroLinea], todoEnUno[numeroLinea + 1], todoEnUno[numeroLinea + 2]]
        #    matriz.append(lista)
         #   numeroLinea += 3


def registrarNuevoUsuarioCedula ():
    # Permitirá almacenar el número de cédula del nuevo usuario.
    intentos = 3
    while intentos>0:
        print("\nSolicitud de número de cédula.")
        cedulaNueva = input("Ingrese el número de cédula, por favor. Nota: Esta no puede ser mayor o menor a 9 dígitos.\nCédula: ")
        if not os.path.exists(cedulaNueva):
            if cedulaNueva.isdigit() and len(cedulaNueva) == 9:
                break
            else:
                intentos -= 1
                print("Su cédula no cumple con nueve dígitos o ya está registrado.")
                cedulaNueva = "0"
        else:
            print("La cédula ya existe.")
            intentos -= 1
            cedulaNueva = "0"
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
def guardarInformacionUsuarios(cedula, nombre, pin):
    archivo = open("Usuarios_y_Pines.txt", 'a')
    archivo.write(cedula)
    archivo.write("\n")
    archivo.write(nombre)
    archivo.write("\n")
    archivo.write(pin)
    archivo.write("\n")
    archivo.close()

def guardarDatosPorUsuario(monedaDolar, monedaColon, monedaBitcoin,cedula):
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
        montoServicio = random.randint(1000, 100000)
        archivo = open(guardarInfoServicios, 'a')
        archivo.write("Tarjeta de Crédito\n")
        archivo.write(str(estadoServicio))
        archivo.write("\n")
        archivo.write(str(montoServicio))
        archivo.close()
    else:
        print("El usuario ", carpetaUsuario, " ya existe.")

def registroNuevoUsuario(matriz):
    while True:
        # Registrar Usuario
        # Permitirá almacenar el número de cédula del nuevo usuario.
        cedula = registrarNuevoUsuarioCedula()
        if cedula == "0":
            break
        else:
            print("Cédula procesada correctamente.")
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
        guardarInformacionUsuarios(cedula, nombre, pin)
        usuario = [cedula, nombre, pin]
        matriz.append(usuario)
        guardarDatosPorUsuario(monedaDolar, monedaColon, monedaBitcoin,cedula)
        break
