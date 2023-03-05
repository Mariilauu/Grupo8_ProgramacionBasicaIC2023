#Fecha: 2/3/2023


while True:
    # Menú Principal
    # Presentará las opciones que se pueden realizar en el cajero.
    print("\nBienvenido.\nMenú Principal")
    print("Por favor digite el número de acuerdo a la opción que aparece en pantalla.")
    opcionMenuPrincipal = int(input("1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: "))
    if opcionMenuPrincipal ==1:
        # Registrar Usuario
        # Permitirá almacenar el número de cédula del nuevo usuario.
        print("Solicitud de número de cédula.")
# Falta contador de intentos para la cédula
        cedulaNueva = int(input("Ingrese el número de cédula, por favor. NOTA: Esta no puede ser mayor o menor a 9 dígitos.\nCédula: "))
# Falta el contador de 9 digitos
# Falta revisar que no esté registrado

        # Solicitud del Nombre.
        # Solicitará el nombre del nuevo usuario.
        print("Solicitud del Nombre.")
        nombreDeUsuario = input("Ingrese su nombre completo, por favor.\nNombre: ")
        # Escogencia del PIN
        print("Escogencia del PIN.")
        pinNuevoUsuario = int(input("Por favor ingrese un PIN de cuatro dígitos. Este le permitirá ingresar a su cuenta.\nPIN:"))
# Falta contador de 4 dígitos
# Falta GETPASS
        while True:
            autentificacionPIN = int(input("Reingrese el PIN para su verificación.\nVerificacón PIN: "))
            if autentificacionPIN == pinNuevoUsuario:
                break
            else:
                print("Su PIN de verificación no coincide con el ingresado incialmente.\nPor favor vuelva a intentarlo")

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
