# Programa que calcula cuántos años faltan para cumplir 100

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Calcular años hasta los 100
años_hasta_100 = 100 - edad

# Convertir el resultado a cadena
años_hasta_100_cadena = str(años_hasta_100)

# Crear un mensaje personalizado
mensaje = "Te faltan " + años_hasta_100_cadena + " años para cumplir 100. ¡Tú puedes!"
print(mensaje)