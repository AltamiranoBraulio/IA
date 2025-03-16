def descuento(precio, porcentaje=18):
    precio_final = precio*(1-porcentaje/100)
    return precio_final