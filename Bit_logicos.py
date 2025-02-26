# Solicitar dos números enteros al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Operaciones lógicas
print("\nOperaciones lógicas:")
print(f"{num1} > {num2} and {num1} < 10: {num1 > num2 and num1 < 10}")
print(f"{num1} > {num2} or {num1} < 10: {num1 > num2 or num1 < 10}")
print(f"not {num1} > {num2}: {not num1 > num2}")

# Operaciones bit a bit
print("\nOperaciones bit a bit:")
print(f"{num1} & {num2} (AND bit a bit): {num1 & num2}")
print(f"{num1} | {num2} (OR bit a bit): {num1 | num2}")
print(f"{num1} ^ {num2} (XOR bit a bit): {num1 ^ num2}")
print(f"~{num1} (NOT bit a bit): {~num1}")
print(f"{num1} << 1 (Desplazamiento a la izquierda): {num1 << 1}")
print(f"{num1} >> 1 (Desplazamiento a la derecha): {num1 >> 1}")