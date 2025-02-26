# Solicitar al usuario que ingrese un número natural
c0 = int(input("Ingresa un número natural (mayor que 0): "))

# Inicializar el contador de pasos
pasos = 0

# Verificar que el número sea válido
if c0 <= 0:
    print("El número debe ser mayor que 0.")
else:
    # Bucle while para aplicar la hipótesis de Collatz
    while c0 != 1:
        # Mostrar el valor actual de c0
        print(c0)
        
        # Aplicar las reglas de Collatz
        if c0 % 2 == 0:  # Si c0 es par
            c0 = c0 // 2
        else:  # Si c0 es impar
            c0 = 3 * c0 + 1
        
        # Incrementar el contador de pasos
        pasos += 1
    
    # Mostrar el último valor (1) y el número de pasos
    print(c0)
    print("pasos =", pasos)