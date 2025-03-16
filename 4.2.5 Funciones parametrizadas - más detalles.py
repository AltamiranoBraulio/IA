def cafe(tipo="americano", tamano="mediano", azucar=1, leche=False, extra=None ):
    descripcion="preparando café {tipo} {tamano}"
    if leche:
        descripcion+=" con leche"
    if extra:
        descripcion+=" y "+extra
    descripcion + f", con {azucar} cucharadas de azúcar"

    return descripcion



print("Bienvenido a la cafeteria")
print("personaliza tu café")
print("De lo contrario dejaremos que el barista decida por ti")
print() 

tipo=input("¿Qué tipo de café te gustaría? (americano, espresso, capuchino, etc.): ") or "americano"
tamano=input("¿Qué tamaño te gustaría? (pequeño, mediano, grande): ") or "mediano"
azucar=int(input("¿Cuántas cucharadas de azúcar te gustaría? (1-3): ") or 1)
leche=input("¿Te gustaría con leche? (si/no): ").lower()=="si"
extra=input("¿Te gustaría algo extra? (canela, chocolate, crema, etc.): ") or None

cafe_personalizado= cafe(tipo=tipo, tamano=tamano, azucar=azucar, leche=leche, extra=extra)

print("\n"+ cafe_personalizado)
print("\n¡Gracias por tu orden!")