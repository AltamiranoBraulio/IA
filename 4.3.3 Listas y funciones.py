def verificar_ingredientes(ingredientes_disponibles):
    ingredientes_necesarios=["masa, queso, salsa, pepperoni, champiñones, aceitunas, pimientos]
    ingredientes_faltantes=[]
    for ingredientes in ingredientes_necesarios:
        if ingredientes not in ingredientes_disponibles:
           ingredientes_faltantes.append(ingredientes)
    if len(ingredientes_faltantes)== 0:
        return "Tienes todos los ingredientes necesarios"
    else:
        return f"Te faltan los siguientes ingredientes: {ingredientes_faltantes}"


mis_ingredientes=["masa", "queso", "salsa", "champiñones", "aceitunas", "pimientos"]

resultado=verificar_ingredientes(mis_ingredientes)
print(resultado)