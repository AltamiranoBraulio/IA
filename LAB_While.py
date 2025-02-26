# Número secreto elegido por el mago
secret_number = 7

# Mensaje inicial del mago
print("""
¡Bienvenido al juego de adivinanza del número secreto!
El mago junior ha elegido un número secreto.
Si no lo adivinas, quedarás atrapado en un bucle para siempre.
¡Buena suerte!
""")

# Bucle para adivinar el número
while True:
    # Solicitar al usuario que ingrese un número
    guess = int(input("Ingresa un número entero: "))
    
    # Verificar si el número es correcto
    if guess == secret_number:
        print(f"¡Bien hecho, muggle! Eres libre ahora. El número secreto era {secret_number}.")
        break  # Salir del bucle
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")