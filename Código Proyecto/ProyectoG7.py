#Fecha: 2/3/2023
def registrarNuevoUsuarioCedula ():
    # Permitirá almacenar el número de cédula del nuevo usuario.
    intentos = 3
    while intentos>0:
        print("\nSolicitud de número de cédula.")
        cedulaNueva = input("Ingrese el número de cédula, por favor. Nota: Esta no puede ser mayor o menor a 9 dígitos.\nCédula: ")
        if cedulaNueva.isdigit() and len(cedulaNueva)==9:
            print("Su número de cédula se ha guardado correctamente.")
            break
        else:
            intentos -= 1
            print("Su cédula no cumple con nueve dígitos o ya está registrado.")
    else:
        print("Vuelva a intentarlo")
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
    while True:
        print("\nEscogencia del PIN.")
        pin = input("Por favor ingrese un PIN de cuatro dígitos. Este le permitirá ingresar a su cuenta.\nPIN:")
        if pin.isdigit() and len(pin) == 4:
            while True:
                autentificacionPIN = (input("Reingrese el PIN para su verificación.\nVerificacón PIN: "))
                if autentificacionPIN == pin:
                    print("Su PIN se ha guardado correctamente.")
                    break
                else:
                    print("Su PIN de verificación no coincide con el ingresado incialmente.\nPor favor vuelva a intentarlo")
            break
        else:
            print("Su PIN debe contener cuatro dígitos.")
    return autentificacionPIN
#***********************************************************************************************************************



# Falta contador de 4 dígitos
# Falta GETPASS


def usuarioRegistrado():
    print("f")
def configuracionAvanzada():
    print("d")

#Programa Principal

while True:
    # Menú Principal
    # Presentará las opciones que se pueden realizar en el cajero.
    print("\nBienvenido.\nMenú Principal")
    print("Por favor digite el número de acuerdo a la opción que aparece en pantalla.")
    opcionMenuPrincipal = int(input("1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: "))
    if opcionMenuPrincipal ==1:
        # Registrar Usuario
        # Permitirá almacenar el número de cédula del nuevo usuario.
        cedula = registrarNuevoUsuarioCedula()
        # Permitirá almacenar el nombre del nuevo usuario.
        nombre = registrarNuevoUsuarioNombre()
        # Permitirá crear un PIN para el nuevo usuario.
        pin = registrarNuevoUsuarioPin()

        archivo=open('Nuevo Usuario.txt', 'a')
        archivo.write(cedula)
        archivo.write("\n")
        archivo.write(nombre)
        archivo.write("\n")
        archivo.write(pin)
        print("\nLa información se ha guardado correctamente.")
        archivo.close()




        # Depósito obligatorio
        print("Depósito obligatorio.")
# Falta la creación de cuenta para cada nuevo usuario y para cada moneda.
        while True:
            #Selección de la moneda
            print("Ingrese la opción de acuerdo al tipo de moneda que desea utilizar para realizar el depósito.")
            monedaDepositoObligatorio = int(input("1.Dolares\n2.Colones\n3.Bitcoins\nOpción: "))
            #Dolares
            if monedaDepositoObligatorio == 1:
                tipoDecambioDolares = 555.80
                montoMinimoDolares = 100000/tipoDecambioDolares
                print("Por favor ingrese una cantidad igual o mayor a ",montoMinimoDolares," dolares.")
                depositoObligatorioDolares = float(input("Depósito: "))
                intentoDepositoObligatorio = 3
                while intentoDepositoObligatorio > 0:
                    if depositoObligatorioDolares >= montoMinimoDolares:
                        break
                    else:
                        intentoDepositoObligatorio -=1
                        print("El monto ingresado es menor al depósito mínimo.")
# Falta volver al menú al terminar los intentos
                break
            #Colones
            elif monedaDepositoObligatorio == 2:
                depositoObligatorioColones = float(input("Por favor ingrese una cantidad igual o mayor a 100 000 colones.\nDepósito: "))
                intentoDepositoObligatorio = 3
                while intentoDepositoObligatorio > 0:
                    if depositoObligatorioColones >= 100000:
                        break
                    else:
                        intentoDepositoObligatorio -= 1
                        print("El monto ingresado es menor al depósito mínimo.")
# Falta volver al menú al terminar los intentos
                break
            #Bitcoins
            elif monedaDepositoObligatorio == 3:
                tipoDecambioBitcoins = 12418330.72
                montoMinimoBitcoins = 100000/tipoDecambioBitcoins
                print("Por favor ingrese una cantidad igual o mayor a ", montoMinimoBitcoins, " dolares.")
                depositoObligatorioBitcoins = float(input("Depósito: "))
                intentoDepositoObligatorio = 3
                while intentoDepositoObligatorio > 0:
                    if depositoObligatorioBitcoins >= montoMinimoBitcoins:
                        break
                    else:
                        intentoDepositoObligatorio -= 1
                        print("El monto ingresado es menor al depósito mínimo.")
#Falta volver al menú al terminar los intentos
                break
            else:
                print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")

        # Seleccionar automática y aleatoriamente tres servicios
#Uso de Biblioteca random
        # Guardar la información del nuevo usuario
#Explicación Estructura del Sistema de Archivos
        # Regresar al menú

    elif opcionMenuPrincipal ==2:
        print("op2")
    elif opcionMenuPrincipal ==3:
        print("op3")
    elif opcionMenuPrincipal ==4:
        print("op4")
    elif opcionMenuPrincipal != 1 or opcionMenuPrincipal != 2 or opcionMenuPrincipal != 3 or opcionMenuPrincipal != 4:
        print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
