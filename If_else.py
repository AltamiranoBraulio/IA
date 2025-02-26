def adivinador_personalidad():
    # Mostrar opciones al usuario
    print("¡Bienvenido al adivinador de personalidad!")
    print("Elige tu animal favorito:")
    print("1. León")
    print("2. Delfín")
    print("3. Águila")

    # Solicitar la elección del usuario
    eleccion = input("Ingresa el número de tu animal favorito (1, 2 o 3): ")

    # Determinar la personalidad basada en la elección
    if eleccion == "1":
        print("\nEres un líder nato. ¡Como el león, tienes un espíritu fuerte y valiente!")
    elif eleccion == "2":
        print("\nEres sociable y amigable. ¡Como el delfín, te encanta conectar con los demás!")
    elif eleccion == "3":
        print("\nEres visionario y libre. ¡Como el águila, buscas siempre alcanzar nuevas alturas!")
    else:
        print("\n¡Ups! No elegiste una opción válida. Intenta de nuevo.")

# Llamar a la función para ejecutar el programa
adivinador_personalidad()