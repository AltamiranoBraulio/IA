def agregar_fruta(inventario, fruta):
    inventario.append(fruta)
    print(f"Fruta agregada: {fruta}")


def manzanas(manazanas_disponibles):
   manzanas_disponibles= 5
   print(f"se modificaron las manzanas ahora son {manzanas_disponibles}")



inventario_frutas = ["manzanas", "peras", "uvas"]

manzanas_en_inventario =10

agregar_fruta(inventario_frutas, "naranjas")
manzanas(manzanas_en_inventario)

print("|nventario de frutas:", inventario_frutas)
print(f"manzanas en inventario: {manzanas_en_inventario}")