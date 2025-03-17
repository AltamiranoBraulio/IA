alumnos = {}
while True:
    nombre = input("Ingresa el nombre del alumno (o deja vacío para terminar): ")
    if nombre == "":
        break  
    calificacion = float(input("Ingresa la calificación del alumno: "))
    if nombre in alumnos:
        alumnos[nombre].append(calificacion)
    else:
        alumnos[nombre] = [calificacion]
print("\n--- Promedios de los alumnos ---")
for nombre, calificaciones in alumnos.items():
    promedio = sum(calificaciones) / len(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre}: {promedio:.2f}")
