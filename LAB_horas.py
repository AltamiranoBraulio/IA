# Programa para calcular la hora final de un evento

# Solicitar la hora de inicio y la duración
hora_inicio = int(input("Ingresa la hora de inicio (0-23): "))
minuto_inicio = int(input("Ingresa el minuto de inicio (0-59): "))
duracion = int(input("Ingresa la duración del evento en minutos: "))

# Calcular los minutos totales
minutos_totales = minuto_inicio + duracion

# Calcular la hora final y los minutos finales
hora_final = (hora_inicio + minutos_totales // 60) % 24
minuto_final = minutos_totales % 60

# Mostrar la hora final
print(f"\nEl evento terminará a las {hora_final:02d}:{minuto_final:02d}")