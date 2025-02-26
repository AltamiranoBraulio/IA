# Programa para calcular el precio total de una compra con IVA

# Solicitar al usuario que ingrese el precio del producto
precio = float(input("Ingresa el precio del producto (en pesos): "))

# Calcular el IVA (16%)
iva = precio * 0.16

# Calcular el precio total
precio_total = precio + iva

# Mostrar los resultados
print("\nDetalle de la compra:")
print(f"Precio del producto: ${precio:.2f} pesos")
print(f"IVA (16%): ${iva:.2f} pesos")
print(f"Precio total: ${precio_total:.2f} pesos")