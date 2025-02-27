def metros_a_kilometros(metros):
    return metros / 1000

def kilogramos_a_gramos(kg):
    return kg * 1000

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir datos al usuario
metros = float(input("Ingresa la cantidad de metros: "))
kg = float(input("Ingresa la cantidad de kilogramos: "))
celsius = float(input("Ingresa la temperatura en °C: "))

# Mostrar resultados
print(f"{metros} metros en kilómetros: {metros_a_kilometros(metros)} km")
print(f"{kg} kilogramos en gramos: {kilogramos_a_gramos(kg)} g")
print(f"{celsius}°C en Fahrenheit: {celsius_a_fahrenheit(celsius)}°F")
