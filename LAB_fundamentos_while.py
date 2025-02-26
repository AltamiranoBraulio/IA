# Solicitar la cantidad de bloques al usuario
bloques = int(input("Ingresa el número de bloques: "))

# Inicializar variables
altura = 0
bloques_necesarios = 0

# Calcular la altura de la pirámide
while bloques_necesarios + (altura + 1) <= bloques:
    altura += 1
    bloques_necesarios += altura

# Imprimir la altura de la pirámide
print("La altura de la pirámide es:", altura)