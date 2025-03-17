# Solicitar el ingreso al usuario
ingreso = float(input("Ingresa tu ingreso anual (en pesos): "))

# Definir el límite para el cálculo del impuesto
limite = 85528

# Calcular el impuesto según las reglas
if ingreso <= limite:
    impuesto = (ingreso * 0.18) - 556.02
else:
    impuesto = 14839.02 + ((ingreso - limite) * 0.32)

# Asegurarse de que el impuesto no sea menor que cero
if impuesto < 0:
    impuesto = 0

# Redondear el impuesto a pesos totales
impuesto_redondeado = round(impuesto)

# Mostrar el resultado
print(f"El impuesto que debes pagar es: {impuesto_redondeado} pesos.")