# Solicitar el año al usuario
año = int(input("Ingresa un año: "))

# Verificar si el año está dentro del período Gregoriano
if año < 1582:
    print("No dentro del período del calendario Gregoriano.")
else:
    # Determinar si el año es bisiesto o común
    if año % 4 != 0:
        print("Año Común")
    elif año % 100 != 0:
        print("Año Bisiesto")
    elif año % 400 != 0:
        print("Año Común")
    else:
        print("Año Bisiesto")