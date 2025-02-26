# Programa para comparar dos números usando == y !=

# Solicitar dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Comparar si los números son iguales
if numero1 == numero2:
    print(f"\n{numero1} es igual a {numero2}.")
else:
    print(f"\n{numero1} no es igual a {numero2}.")

# Comparar si los números son diferentes
if numero1 != numero2:
    print(f"{numero1} es diferente de {numero2}.")
else:
    print(f"{numero1} no es diferente de {numero2}.")