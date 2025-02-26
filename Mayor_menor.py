# Solicitar dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Usar un diccionario para determinar la relación
resultado = {
    numero1 > numero2: f"{numero1} es mayor que {numero2}",
    numero1 < numero2: f"{numero1} es menor que {numero2}",
    numero1 == numero2: f"{numero1} es igual a {numero2}"
}

# Seleccionar el resultado correcto
print(resultado[True])