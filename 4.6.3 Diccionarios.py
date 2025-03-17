agenda = {}
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado con éxito.")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")
