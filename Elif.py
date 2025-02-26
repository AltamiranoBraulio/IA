def recomendador_peliculas():
    print("¡Bienvenido al Recomendador de Películas!")
    print("Elige tu género de película favorito:")
    print("1. Acción")
    print("2. Comedia")
    print("3. Terror")
    print("4. Ciencia Ficción")
    print("5. Drama")

    # Solicitar la elección del usuario
    eleccion = input("Ingresa el número de tu género favorito (1-5): ")

    # Recomendar una película basada en la elección
    if eleccion == "1":
        print("\nTe recomiendo: 'John Wick' (Acción). ¡Llena de peleas intensas y emociones fuertes!")
    elif eleccion == "2":
        print("\nTe recomiendo: 'Supercool' (Comedia). ¡Una comedia clásica llena de situaciones divertidas!")
    elif eleccion == "3":
        print("\nTe recomiendo: 'El Conjuro' (Terror). ¡Perfecta para los amantes del miedo!")
    elif eleccion == "4":
        print("\nTe recomiendo: 'Interestelar' (Ciencia Ficción). ¡Una aventura épica en el espacio!")
    elif eleccion == "5":
        print("\nTe recomiendo: 'Forrest Gump' (Drama). ¡Una historia conmovedora y llena de emociones!")
    else:
        print("\n¡Ups! No elegiste una opción válida. Intenta de nuevo.")

# Llamar a la función para ejecutar el recomendador
recomendador_peliculas()