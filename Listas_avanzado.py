# Programa para simular una estación meteorológica que registra temperaturas cada hora durante un mes

import random

# Crear una lista bidimensional para almacenar las temperaturas (31 días x 24 horas)
# Usamos comprensión de listas para inicializar la matriz con valores aleatorios
temperaturas = [[round(random.uniform(-10, 40), 1) for h in range(24)] for d in range(31)]

# Función para mostrar la temperatura de un día y hora específicos
def consultar_temperatura(dia, hora):
    if 0 <= dia < 31 and 0 <= hora < 24:
        return temperaturas[dia][hora]
    else:
        return None  # Fuera de rango

# Mostrar algunas temperaturas de ejemplo
print("Temperaturas de ejemplo (primeros 3 días):")
for dia in range(3):  # Mostrar solo los primeros 3 días para no saturar la salida
    print(f"Día {dia + 1}: {temperaturas[dia]}")

# Interacción con el usuario
while True:
    try:
        # Pedir al usuario que ingrese un día y una hora
        dia = int(input("\nIngresa el día del mes (1-31): ")) - 1  # Restar 1 para convertir a índice
        hora = int(input("Ingresa la hora del día (0-23): "))

        # Consultar la temperatura
        temp = consultar_temperatura(dia, hora)
        if temp is not None:
            print(f"La temperatura el día {dia + 1} a las {hora}:00 fue de {temp}°C.")
        else:
            print("¡Día u hora fuera de rango! Intenta de nuevo.")
    except ValueError:
        print("¡Entrada inválida! Ingresa números enteros.")