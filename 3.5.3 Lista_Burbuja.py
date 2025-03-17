# Función para ordenar una lista usando el algoritmo de ordenamiento burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista inicial desordenada
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)

# Ordenar la lista usando el algoritmo de ordenamiento burbuja
ordenamiento_burbuja(lista)
print("Lista ordenada:", lista)