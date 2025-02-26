# Función para mostrar la representación binaria de un número
def mostrar_binario(numero, bits=8):
    return format(numero, f'0{bits}b')

# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Mostrar el número en binario
print(f"\nEl número {numero} en binario es: {mostrar_binario(numero)}")

# Desplazamiento a la izquierda
desplazamiento_izquierda = numero << 1
print(f"\nDesplazamiento a la izquierda (<< 1):")
print(f"Resultado: {desplazamiento_izquierda}")
print(f"Binario: {mostrar_binario(desplazamiento_izquierda)}")

# Desplazamiento a la derecha
desplazamiento_derecha = numero >> 1
print(f"\nDesplazamiento a la derecha (>> 1):")
print(f"Resultado: {desplazamiento_derecha}")
print(f"Binario: {mostrar_binario(desplazamiento_derecha)}")