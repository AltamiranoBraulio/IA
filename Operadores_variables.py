import math  # Necesario para la raíz cuadrada

# Entrada de datos
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))

# Cálculos
area = longitud * ancho  # Área del rectángulo
perimetro = 2 * (longitud + ancho)  # Perímetro del rectángulo
raiz_cuadrada = math.sqrt(numero)  # Raíz cuadrada del número

# Operaciones adicionales
potencia = numero ** 2  # Elevar al cuadrado el número
division_entera = area // perimetro  # División entera entre área y perímetro
modulo = area % perimetro  # Residuo de dividir área entre perímetro

# Actualización de una variable con un nuevo valor (doble del área)
nuevo_valor = area * 2

# Mostrar resultados
print("\n========== RESULTADOS ==========")
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)
print(f"La raíz cuadrada de {numero} es:", round(raiz_cuadrada, 2))
print(f"{numero} elevado al cuadrado es:", potencia)
print("La división entera del área y el perímetro es:", division_entera)
print("El residuo de dividir área entre perímetro es:", modulo)
print("El nuevo valor (doble del área) es:", nuevo_valor)
