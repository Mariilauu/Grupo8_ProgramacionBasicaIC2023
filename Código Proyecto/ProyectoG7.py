#Fecha: 2/3/2023

#Menú Principal
#Presentará las opciones que se pueden realizar en el cajero.
opcionMenuPrincipal = int(input("Bienvenido.\n Por favor digite el número de acuerdo a la opción que aparece en pantalla.\n1. Registrar nuevo usuario\n2. Usuario Registrado\n3. Configuración Avanzada\n4. Salir\nDigite su opción aquí: "))
while opcionMenuPrincipal != 1 or opcionMenuPrincipal != 2 or opcionMenuPrincipal != 3 or opcionMenuPrincipal != 4:
    print("La opción ingresada no corresponde a ninguna de las anteriores.")
if opcionMenuPrincipal ==1:
    #Registrar Usuario
    #Permitirá almacenar el número de cédula del nuevo usuario.
    cedulaNueva = int(input("Ingrese el número de cédula, por favor. NOTA: Esta no puede ser mayor o menor a 9 dígitos.\nCédula: "))
    # Solicitud del Nombre.
    # Solicitará el nombre del nuevo usuario.
    nombreDeUsuario = input("Ingrese su nombre completo, por favor.\nNombre: ")
    #Escogencia del PIN
    #Permite que el usuario acceda a su cuenta.
    pinNuevoUsuario = int(input("Ingrese un PIN de cuatro (4) dígitos, por favor. Este le permitirá ingresar a su cuenta luego que la cuenta sea creada.\nPIN:"))
#AGREGAR GETPASS
    verificarUsuario = int(input("Por favor reingrese el PIN para su verificación.\nVerificación del PIN: "))
    while pinNuevoUsuario != verificarUsuario:
        print("El PIN de verificación no coincide con el PIN inicial.\nPor favor vuelva a intentarlo.")

    #Depósito obligatorio
    print("Ahora se procederá a hacer el depósito obligatorio que le permitirá completar su registro.")
    monedaDepositoObligatorio = input("Por favor ingrese la moneda que desea utilizar para hacer el depósito.\n1. Dolares\n2. Colones\nMoneda: ")
    while monedaDepositoObligatorio != 1 or monedaDepositoObligatorio !=2:
        print("La opción ingresada no corresponde a ninguna de las anteriores.")
    if monedaDepositoObligatorio ==1:
        depositoObligatorioDolares = int(input("Por favor realize un depósito igual o mayor a $180.\nIngrese la cantidad, por favor: "))
        while depositoObligatorioDolares <180:
            print("El monto ingresado es menor al necesario para realizar el depósito obligatorio.")
    elif monedaDepositoObligatorio ==2:
        depositoObligatorioColones = int(input("Por favor realiza un depósito igual o mayor a ₡100 000.\nIngrese la cantidad, por favor: "))
        while depositoObligatorioColones <100000:
            print("El monto ingresado es menor al necesario para realizar el depósito obligatorio.")
#Faltan los 3 intentos
    #Seleccionar automática y aleatoriamente tres servicios

    #Guardar la información del nuevo usuario

    #Regresar al menú


