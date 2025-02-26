# Pedimos al usuario que ingrese una cantidad de segundos
segundos = int(input("Ingresa una cantidad de segundos: "))

# Calculamos las horas, minutos y segundos
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

# Imprimimos el resultado de la conversión
print(f"{segundos} segundos son equivalentes a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
