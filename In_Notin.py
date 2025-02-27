# Script para demostrar el uso de "in" y "not in" en listas

# Lista de nombres
nombres = ["Ana", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel"]

# Mostrar la lista de nombres
print("Lista de nombres:", nombres)

# Pedir al usuario que ingrese un nombre para buscar
nombre_buscado = input("Ingresa un nombre para verificar si está en la lista: ")

# Verificar si el nombre está en la lista usando "in"
if nombre_buscado in nombres:
    print(f"¡Sí! '{nombre_buscado}' está en la lista.")
else:
    print(f"¡No! '{nombre_buscado}' no está en la lista.")

# Verificar si el nombre NO está en la lista usando "not in"
if nombre_buscado not in nombres:
    print(f"¿Sabías que '{nombre_buscado}' no está en la lista?")
else:
    print(f"¿Sabías que '{nombre_buscado}' sí está en la lista?")