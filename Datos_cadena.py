# Programa de historia interactiva usando cadenas (strings) y print

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
lugar = input("Ingresa un lugar: ")
objeto = input("Ingresa un objeto: ")
accion = input("Ingresa una acción (en infinitivo, como 'correr' o 'saltar'): ")

# Crear la historia
historia = f"\nHabía una vez una persona llamada {nombre}, que vivía en {lugar}. \
Un día, {nombre} encontró un {objeto} mágico. Decidió {accion} con él, \
y así comenzó una gran aventura. ¡Fin!"

# Mostrar la historia
print(historia)