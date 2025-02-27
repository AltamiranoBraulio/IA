# Programa para registrar notas de estudiantes y calcular sus promedios

# Lista de estudiantes con sus respectivas notas (listas anidadas)
estudiantes = [
    [1, "Ana", [85, 90, 78]],  # Estudiante 1: ID, Nombre, Lista de notas
    [2, "Carlos", [92, 88, 91]],  # Estudiante 2
    [3, "Diana", [76, 81, 79]],  # Estudiante 3
    [4, "Eduardo", [89, 93, 87]],  # Estudiante 4
    [5, "Fernanda", [95, 96, 94]]  # Estudiante 5
]

# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)  # Suma de notas dividida por la cantidad de notas

# Mostrar la información de cada estudiante y su promedio
print("Registro de notas de estudiantes:")
for estudiante in estudiantes:
    id_estudiante, nombre, notas = estudiante  # Desempaquetar la lista anidada
    promedio = calcular_promedio(notas)  # Calcular el promedio
    print(f"ID: {id_estudiante}, Nombre: {nombre}, Notas: {notas}, Promedio: {promedio:.2f}")

# Búsqueda de un estudiante por ID (interacción con el usuario)
id_buscado = int(input("\nIngresa el ID de un estudiante para ver sus notas: "))

# Buscar el estudiante en la lista
encontrado = False
for estudiante in estudiantes:
    if estudiante[0] == id_buscado:  # Comparar el ID buscado con el ID del estudiante
        encontrado = True
        nombre = estudiante[1]
        notas = estudiante[2]
        promedio = calcular_promedio(notas)
        print(f"\nEstudiante encontrado:")
        print(f"ID: {id_buscado}, Nombre: {nombre}, Notas: {notas}, Promedio: {promedio:.2f}")
        break

if not encontrado:
    print(f"No se encontró ningún estudiante con el ID {id_buscado}.")