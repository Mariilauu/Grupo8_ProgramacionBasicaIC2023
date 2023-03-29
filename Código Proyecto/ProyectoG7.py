#Fecha: 2/3/2023

# Para cargar la información de los usuarios desde el arreglo
def cargar_usuarios():
    return usuarios

# Hacer el sub menu indicado
def autenticar_usuario():
    cedula = input("Ingrese su cedula: ")
    if cedula in usuarios:
        usuario = usuarios[cedula]
        intentos_pin = 3
        while intentos_pin > 0:
            pin = input("Ingrese su PIN: ")
            if pin == usuario["pin"]:
                print(f"Bienvenido {usuario['nombre']}!")
                return usuario
            else:
                intentos_pin -= 1
                print("PIN incorrecto. Intente de nuevo.")
        print("Se excedió el máximo de intentos para ingresar su PIN. Volviendo al menú principal.")
        return None
    else:
        print("Cedula invalida. Volviendo al menú principal.")
        return None


def pagar_servicio(usuario):
    servicio = input("Ingrese el nombre del servicio a pagar: ")
    if servicio in usuario["servicios"]:
        monto = usuario["servicios"][servicio]
        if monto <= usuario["saldo"]:
            usuario["saldo"] -= monto
            del usuario["servicios"][servicio]
            print(f"Pago de servicio exitoso. Saldo actual: {usuario['saldo']}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Servicio no encontrado.")

def retirar_dinero(usuario):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= usuario["saldo"]:
        usuario["saldo"] -= monto
        print(f"Retiro exitoso. Saldo actual: {usuario['saldo']}")
    else:
        print("Saldo insuficiente.")


def depositar_dinero(usuario):
    monto = float(input("Ingrese el monto a depositar: "))
    usuario["saldo"] += monto
    print(f"Deposito exitoso. Saldo actual: {usuario['saldo']}")


def ver_saldo(usuario):
    print(f"Su saldo actual es: {usuario['saldo']}")


def compra_venta_divisas(usuario):
    print("Funcion no implementada.")


def eliminar_usuario():
    cedula = input("Ingrese la cedula del usuario a eliminar: ")
    if cedula in usuarios:
        del usuarios[cedula]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")


def menu():
    print("Bienvenido al sistema bancario.")
    while True:
        print("""
        1. Autenticación de usuario
        2. Retirar dinero
        3. Depositar dinero
        4. Ver saldo actual
        5. Pagar servicios
        6. Compra/Venta de Divisas
        7. Eliminar usuario
        8. Salir""")

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

        usuarios = []

        # Solicitamos al usuario que ingrese su nombre
        nombre = input("Por favor, ingrese su nombre: ")

        # Agregamos la información del usuario a la lista
        usuarios.append({"nombre": nombre})

        # Mostramos un mensaje de confirmación
        print("¡Hola, {}! Tu información ha sido guardada correctamente.".format(nombre))

        # Después de cargar los usuarios
        usuarios = cargar_usuarios()

        if len(usuarios) == 0:
            print("No hay usuarios registrados")
            # Volver al menú principal
            # Continuar con la autenticación de usuarios
        # Después de verificar que hay usuarios registrados
        intentos_cedula = 3
        intentos_pin = 3

        while intentos_cedula > 0:
            cedula = input("Ingrese su número de cédula: ")
            # Validar que la cédula sea un número y que esté registrada
            for usuario in usuarios:
                if usuario.cedula == cedula:
                    while intentos_pin > 0:
                        pin = input("Ingrese su PIN: ")
                        # Validar que el PIN sea correcto
                        if usuario.validar_pin(pin):
                            # Continuar con las opciones del menú
                            break
                        else:
                            intentos_pin -= 1
                            if intentos_pin == 0:
                                print(
                                    "Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal")
                                # Volver al menú principal
                            else:
                                print("PIN incorrecto, le quedan", intentos_pin, "intentos")
                    break
            else:
                intentos_cedula -= 1
                if intentos_cedula == 0:
                    print("Se excedió el máximo de intentos para ingresar su cédula, volviendo al menú principal")
                    # Volver al menú principal
                else:
                    print("Cédula no registrada, le quedan", intentos_cedula, "intentos")

    elif opcionMenuPrincipal ==3:
        print("op3")
    elif opcionMenuPrincipal ==4:
        print("op4")
    elif opcionMenuPrincipal != 1 or opcionMenuPrincipal != 2 or opcionMenuPrincipal != 3 or opcionMenuPrincipal != 4:
        print("El valor ingresado no corresponde a ninguna de las opciones anteriores.")
