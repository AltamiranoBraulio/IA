    # Lista inicial de edades de estudiantes
edades_estudiantes = [18, 19, 20, 21, 22]
print("Edades iniciales de los estudiantes:", edades_estudiantes)

# Paso 1: Reemplazar la edad central
nueva_edad = int(input("\nIngresa una nueva edad para reemplazar la edad central (20): "))
edades_estudiantes[2] = nueva_edad  # El índice 2 es la edad central (20)
print("Edades después de reemplazar la edad central:", edades_estudiantes)

# Paso 2: Eliminar la última edad
edad_eliminada = edades_estudiantes.pop()  # Elimina la última edad de la lista
print(f"\nSe eliminó la última edad: {edad_eliminada}")
print("Edades después de eliminar la última edad:", edades_estudiantes)

# Paso 3: Imprimir la longitud de la lista
longitud_lista = len(edades_estudiantes)
print(f"\nLa cantidad actual de edades en la lista es: {longitud_lista}")