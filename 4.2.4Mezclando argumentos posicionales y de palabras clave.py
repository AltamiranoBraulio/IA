def descuento(precio, nombre, porcentaje=18, aplicable=True):
    if aplicable:
        precio_descuento = precio*(1-porcentaje/100)
    else:
        precio_descuento = precio
        print(f"El producto {nombre}")
        print(f"Precio original ${precio}")
        print(f"Descuento del {porcentaje}%")
        print(f"Total a pagar ${precio_descuento}")
        print()
        print()

descuento(1000, "Laptop", 10)
descuento(500, "Tablet", 15, False)     
descuento(200, "iPhone", 20)    
descuento(300, "Smartwatch", 5, False)
    