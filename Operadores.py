# Pedimos datos al usuario
subtotal = float(input("Ingresa el subtotal de la comida (MXN): "))
impuesto = float(input("Ingresa el porcentaje de impuestos (ej. 16 para 16%): ")) / 100
propina = float(input("Ingresa el porcentaje de propina (ej. 10 para 10%): ")) / 100
personas = int(input("¿Entre cuántas personas se dividirá la cuenta?: "))

# Cálculos
total_con_impuesto = subtotal + (subtotal * impuesto)
total_a_pagar = total_con_impuesto + (subtotal * propina)
pago_por_persona = total_a_pagar / personas

# Otros cálculos con operadores adicionales
residuo = total_a_pagar % personas  # ¿Sobra algo al dividir la cuenta?
division_entera = total_a_pagar // personas  # Pago sin centavos
propina_cuadrada = (subtotal * propina) ** 2  # Solo para jugar con exponentes

# Mostramos los resultados
print("\n========== RESULTADOS ==========")
print("Subtotal:", subtotal, "MXN")
print("Total con impuestos:", round(total_con_impuesto, 2), "MXN")
print("Total a pagar (con propina):", round(total_a_pagar, 2), "MXN")
print("Cada persona paga:", round(pago_por_persona, 2), "MXN")
print("Residuo de la división:", round(residuo, 2))
print("Pago por persona (sin centavos):", round(division_entera, 2))
print("Propina al cuadrado (dato random):", round(propina_cuadrada, 2))
