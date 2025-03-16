def cafe(tipo="americano", tamano="mediano", azucar=1, leche=false, extra=None ):
    descricion="preparando café {tipo} {tamano}"
    if leche:
        descricion+=" con leche"
    if extra:
        descricion+=" y "+extra
    descricion + f", con {azucar} cucharadas de azúcar"

return descricion



print("Bienvenido a la cafeteria")
print("personaliza tu café")
print("De lo contrario dejaremos que el barista decida por ti")
print() 

tipo=input("¿Qué tipo de café te gustaría? (americano, espresso, capuchino, etc.): ") or "americano"
tamano=input("¿Qué tamaño te gustaría? (pequeño, mediano, grande): ") or "mediano"
azucar=int(input("¿Cuántas cucharadas de azúcar te gustaría? (1-3): ") or 1)
leche=input("¿Te gustaría con leche? (si/no): ").lower()=="si"
extra=input("¿Te gustaría algo extra? (canela, chocolate, crema, etc.): ") or None

