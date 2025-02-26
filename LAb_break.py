# Bucle while para pedir una palabra al usuario
while True:
    palabra = input("Ingresa una palabra: ")  # Solicitar la palabra al usuario
    
    # Verificar si la palabra es "chupacabra"
    if palabra == "chupacabra":
        print("Has dejado el bucle con éxito.")
        break  # Salir del bucle