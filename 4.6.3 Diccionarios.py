# Crear una agenda vacía
agenda = {}

def agregar_contacto(nombre, telefono):
    """
    Agrega un contacto a la agenda.
    """
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con éxito.")

def buscar_contacto(nombre):
    """
    Busca un contacto en la agenda por su nombre.
    """
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")

def mostrar_agenda():
    """
    Muestra todos los contactos en la agenda.
    """
    if agenda:
        print("\n--- Agenda de contactos ---")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")


# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar agenda")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        mostrar_agenda()
    elif opcion == "4":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")