# Paso 1: Crear una lista vacía llamada beatles
beatles = []
print("Paso 1:", beatles)

# Paso 2: Agregar a John Lennon, Paul McCartney y George Harrison usando append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# Paso 3: Usar un bucle for y append() para agregar a Stu Sutcliffe y Pete Best
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    beatles.append(miembro)
print("Paso 3:", beatles)

# Paso 4: Usar la instrucción del para eliminar a Stu Sutcliffe y Pete Best
del beatles[3]  # Elimina a Stu Sutcliffe (índice 3)
del beatles[3]  # Elimina a Pete Best (índice 3)
print("Paso 4:", beatles)

# Paso 5: Usar insert() para agregar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

# Pregunta adicional
print("\n¿Eres fan de los Beatles? ¡Son una de las bandas favoritas de Greg!")