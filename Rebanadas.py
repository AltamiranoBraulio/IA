# Juego de adivinanza de números
# La computadora elige un número aleatorio entre 1 y 100, y el usuario debe adivinarlo.

import random  # Solo para generar el número aleatorio, pero no usamos funciones avanzadas.

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar variables
intentos = 0
adivinado = False  # Booleano para controlar si el usuario ha adivinado

# Mensaje de bienvenida
print("¡Bienvenido al juego de adivinanza de números!")
print("He elegido un número entre 1 y 100. ¿Puedes adivinarlo?")

# Ciclo principal del juego
while not adivinado:  # Mientras el usuario no haya adivinado
    # Pedir al usuario que ingrese un número
    intento = int(input("Ingresa tu número: "))
    intentos += 1  # Incrementar el contador de intentos

    # Comparar el número ingresado con el número secreto
    if intento < numero_secreto:
        print("Demasiado bajo. ¡Intenta de nuevo!")
    elif intento > numero_secreto:
        print("Demasiado alto. ¡Intenta de nuevo!")
    else:
        # Si el número es correcto, cambiar el booleano a True
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

# Fin del juego
print("¡Gracias por jugar!")