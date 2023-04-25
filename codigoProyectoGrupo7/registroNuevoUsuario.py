# Primera opción del menú ubicado en programa principal.
# Crea un usuario nuevo (cedula, nombre, pin y hace depósito obligatorio)
# Guarda los datos en archivos.

#Bibliotecas importadas
import os
import random
import comun
import getpass

#***********************************************************************************************************************

#Función para registrar la cédula para un nuevo usuario
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

#Función para registrar el nombre del nuevo usuario
def registrarNuevoUsuarioNombre ():
    # Solicitud del Nombre.
    print("\nSolicitud del Nombre.")
    while True:
        nombreDeUsuario = input("Ingrese su nombre completo, por favor.\nNombre: ")
        if len(nombreDeUsuario)>0:
            break
    return nombreDeUsuario

#***********************************************************************************************************************

#Función para registrar el pin del nuevo usuario
def registrarNuevoUsuarioPin():
    # Escogencia del PIN
# Falta GETPASS
    while True:
        print("\nEscogencia del PIN.")
        pin = (getpass.getpass(prompt="Por favor ingrese un PIN de cuatro dígitos. Este le permitirá ingresar a su cuenta.\nPIN: "))
        if pin.isdigit() and len(pin) == 4:
            while True:
                autentificacionPIN = (getpass.getpass(prompt="Reingrese el PIN para su verificación.\nVerificacón PIN: "))
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
#Función para depósito en dólares
def dolares(tiposCambio):
    tipoDecambioDolares = tiposCambio[1]
    montoMinimoDolares = 100000 / float(tipoDecambioDolares)

    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio>0:
        print("\nPor favor ingrese una cantidad igual o mayor a ", montoMinimoDolares, " dolares.")
        depositoObligatorioDolares = float(comun.capturaMonto("Depósito: ", 1))
        if depositoObligatorioDolares >= montoMinimoDolares:
            return str(depositoObligatorioDolares)
        else:
            depositoObligatorioDolares ="0"
            print("El monto ingresado es menor al depósito mínimo.")
            intentoDepositoObligatorio -= 1
    return depositoObligatorioDolares

#*********************************************************

#Función para depósito en colones
def colones(tiposCambio):
    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio > 0:
        depositoObligatorioColones = float(comun.capturaMonto("\nPor favor ingrese una cantidad igual o mayor a 100 000 colones.\nDepósito: ", 1))
        if depositoObligatorioColones >= 100000:
            return str(depositoObligatorioColones)
        else:
            depositoObligatorioColones = "0"
            intentoDepositoObligatorio -= 1
            print("El monto ingresado es menor al depósito mínimo.")
    return depositoObligatorioColones

#*********************************************************

#Función para depósito en bitcoins
def bitcoins(tiposCambio):
    tipoDecambioBitcoins = tiposCambio[6]
    montoMinimoBitcoins = 100000 / float(tipoDecambioBitcoins)
    intentoDepositoObligatorio = 3
    while intentoDepositoObligatorio > 0:
        print("\nPor favor ingrese una cantidad igual o mayor a ", montoMinimoBitcoins, " bitcoins.")
        depositoObligatorioBitcoins = float(comun.capturaMonto("Depósito: ", 1))
        if depositoObligatorioBitcoins >= montoMinimoBitcoins:
            return str(depositoObligatorioBitcoins)
        else:
            depositoObligatorioBitcoins ="0"
            intentoDepositoObligatorio -= 1
            print("El monto ingresado es menor al depósito mínimo.")
    return depositoObligatorioBitcoins

#***********************************************************************************************************************

#Función para guardar cedula, nombre y pin, una vez creado el usuario
def guardarInformacionUsuarios(cedula, nombre, pin):
    archivo = open(comun.NombreArchivoUsuarios, 'a')
    archivo.write(cedula)
    archivo.write("\n")
    archivo.write(nombre)
    archivo.write("\n")
    archivo.write(pin)
    archivo.write("\n")
    archivo.close()

#***********************************************************************************************************************

#Función para guardar los saldos del usuario (cuentas en dolar, colones y bitcoins) y crear los servicios de forma aleatoria
def guardarDatosPorUsuario(monedaDolar, monedaColon, monedaBitcoin,cedula):
    carpetaUsuario = cedula
    if not os.path.exists(carpetaUsuario):
        os.makedirs(carpetaUsuario)
        infoSaldos = "saldos.txt"
        guardarInfoSaldos = os.path.join(carpetaUsuario, infoSaldos)

#Guarda montos en cuentas
        archivo = open(guardarInfoSaldos, 'a')
        archivo.write(monedaDolar)
        archivo.write("\n")
        archivo.write(monedaColon)
        archivo.write("\n")
        archivo.write(monedaBitcoin)
        archivo.close()

#Crea de forma aleatoria servicio 1
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

#Crea de forma aleatoria servicio 2
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

# Crea de forma aleatoria servicio 3
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

# Crea de forma aleatoria servicio 4
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

# Crea de forma aleatoria servicio 5
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

# Crea de forma aleatoria servicio 6
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

# Crea de forma aleatoria servicio 7
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

#***********************************************************************************************************************

#Función principal donde se unen las funciones de registroNuevoUsuarioCedula, registroNuevoUsuarioNombre y registroNuevoUsuarioPin
#así como cada una de las funciones de las monedas
def registroNuevoUsuario(matriz,tipoCambio):
    # Registrar Usuario
    # Permitirá almacenar el número de cédula del nuevo usuario.
    cedula = registrarNuevoUsuarioCedula()
    if cedula == "0":
        print("Se excedió el máximo de intentos para ingresar un número de cédula válido, volviendo al menú principal.")
        return
    else:
        print("Cédula procesada correctamente.")
    # Permitirá almacenar el nombre del nuevo usuario.
    nombre = registrarNuevoUsuarioNombre()
    # Permitirá crear un PIN para el nuevo usuario.
    pin = registrarNuevoUsuarioPin()
    if pin.isdigit() and len(pin) == 4:
        print("Su PIN ha sido validado.")
    else:
        return
    # Permitirá hacer un depósito
    print("\nDepósito obligatorio.")
    monedaDolar = "0"
    monedaColon = "0"
    monedaBitcoin = "0"
    while True:
        # Selección de la moneda
        print("Ingrese la opción de acuerdo al tipo de moneda que desea utilizar para realizar el depósito.")
        monedaDepositoObligatorio = input("1.Dolares\n2.Colones\n3.Bitcoins\nOpción: ")
        if monedaDepositoObligatorio == "1":
            monedaDolar = dolares(tipoCambio)
            break
        elif monedaDepositoObligatorio == "2":
            monedaColon = colones(tipoCambio)
            break
        elif monedaDepositoObligatorio == "3":
            monedaBitcoin = bitcoins(tipoCambio)
            break
        else:
            print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
    #Guarda los datos
    if monedaDolar != "0" or monedaColon != "0" or monedaBitcoin != "0":
        guardarInformacionUsuarios(cedula, nombre, pin)
        usuario = [cedula, nombre, pin]
        matriz.append(usuario)
        guardarDatosPorUsuario(monedaDolar, monedaColon, monedaBitcoin, cedula)
        print("El usuario fue creado de forma exitosa.")