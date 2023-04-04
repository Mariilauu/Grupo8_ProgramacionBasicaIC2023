import os
#configuracion avanzada
# Ruta de los archivos de texto plano
USUARIOS_FILE = "usuarios.txt"
TIPOS_CAMBIO_FILE = "tipos_cambio.txt"
CONFIG_FILE = "config.txt"

def solicitarPinEspecial():
    pin = input("Ingrese el PIN especial: ")
    if config.get == null
        print("El PIN especial no existe.")
        registrarNuevoUsuarioCedula()
    with open(CONFIG_FILE, 'r') as f:
        config = dict(line.strip().split('=') for line in f)
    if pinEspecial == config.get('PIN_especial'):
        print("Bienvenido al modo especial")
    else:
        print("El PIN especial es incorrecto.")
        return
    
def eliminarUsuario():
    usuario = input("Ingrese el nombre de usuario a eliminar: ")
    usuarios = {}
    with open(USUARIOS_FILE, 'r') as f:
        for line in f:
            user, pwd = line.strip().split(':')
            usuarios[user] = pwd
    if usuario in usuarios:
        del usuarios[usuario]
        with open(USUARIOS_FILE, 'w') as f:
            for user, pwd in usuarios.items():
                f.write(f"{user}:{pwd}\n")
        # Eliminar carpetas y archivos de usuario
        path = os.path.join("data", usuario)
        if os.path.exists(path):
            shutil.rmtree(path)
        print("El usuario ha sido eliminado")
        mostrarMenu()
    else:
        print("El usuario no existe")
        mostrarMenu()
def modificarTiposDeCambio():
    tiposDeCambio = {}
    with open(TIPOS_CAMBIO_FILE, 'r') as f:
        for line in f:
            divisa, tasa = line.strip().split('=')
            tiposDeCambio[divisa] = float(tasa)
    print("Tipos de cambio actuales:")
    for divisa, tasa in tiposDeCambio.items():
        print(f"{divisa}: {tasa}")
    divisa = input("Ingrese la divisa a modificar (ejemplo: USD): ")
    if divisa in tiposDeCambio:
        while True:
            try:
                tasa = float(input(f"Ingrese la nueva tasa para {divisa}: "))
                if tasa <= 0:
                    raise ValueError("La tasa debe ser mayor que cero")
                break
            except ValueError as e:
                print("Error: " + str(e))
        tiposDeCambio[divisa] = tasa
        with open(TIPOS_CAMBIO_FILE, 'w') as f:
            for divisa, tasa in tiposDeCambio.items():
                f.write(f"{divisa}={tasa}\n")
        print(f"La tasa para {divisa} ha sido actualizada")
        mostrarMenu()
    else:
        print("Divisa no encontrada")
        mostrarMenu()

def main():
    solicitarPinEspecial()
    # Comprobar si los archivos de texto plano existen, y crearlos si no existen
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'w') as f:
            f.write("usuario1:contrasena1\nusuario2:contrasena2\n")
    if not os.path.exists(TIPOS_CAMBIO_FILE):
        with open(TIPOS_CAMBIO_FILE, 'w') as f:
            f.write("USD=500.0\nEUR=600.0\n")
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            f.write("PIN_especial=1234\n")
    mostrarMenu()
    
def mostrarMenu():
        print("1. Eliminar usuario")
        print("2. Modificar tipos de cambio")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            eliminarUsuario()
        elif opcion == "2":
            modificarTiposDeCambio()
        elif opcion == "3":
            print("Saliendo...")
            return
        else:
            print("Opción inválida")
            mostrarMenu()

main()
