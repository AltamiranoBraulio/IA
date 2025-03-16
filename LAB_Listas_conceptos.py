# Pedir al usuario que ingrese una lista de números
entrada_usuario = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números enteros
lista_original = list(map(int, entrada_usuario.split()))

# Lista temporal para almacenar números únicos
lista_sin_repetidos = []

# Recorrer la lista original
for numero in lista_original:
    # Si el número no está en la lista temporal, agregarlo
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

# Mostrar la lista original y la lista sin repeticiones
print("Lista original:", lista_original)
print("Lista sin repeticiones:", lista_sin_repetidos)