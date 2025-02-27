# Programa para demostrar el uso de listas e índices negativos

# Crear una lista de elementos
lista = ["manzana", "banana", "cereza", "dátil", "frambuesa", "granada"]

# Mostrar la lista al usuario
print("Lista de frutas:", lista)

# Pedir al usuario que ingrese un índice (puede ser positivo o negativo)
indice = int(input("Ingresa un índice del 0 al 5 para acceder a un elemento de la lista: "))

# Acceder al elemento usando el índice
try:
    elemento = lista[indice]  # Los índices negativos acceden desde el final de la lista
    print(f"El elemento en el índice {indice} es: {elemento}")
except IndexError:
    print("¡Error! El índice está fuera del rango de la lista.")

