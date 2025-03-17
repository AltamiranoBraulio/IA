def chicles (chicles_disponibles):
    if chicles_disponibles > 0:
        return "chicles"
    else:
        return None
    

comprar = chicles(3)
if comprar is not None:
    print(f"obtuviste un paquete de {comprar}")
else:   
    print("Producto no disponible")

comprar = chicles(0)
if comprar is not None:
    print(f"obtuviste un paquete de {comprar}")
else:   
     print("Producto no disponible")
