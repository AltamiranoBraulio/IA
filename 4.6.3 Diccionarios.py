agenda = {}
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con éxito.")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")
def mostrar_agenda():
    if agenda:
        print("\n--- Agenda de contactos ---")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
while True:
    print("\n--- Menú ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar agenda")
    print("4. Salir")
