visitas_totales = 0

def vistas():
    global visitas_totales
    visitas_totales += 1
    print(f"Visita registrada. Total de visitas: {visitas_totales}")

def resteo():
    global visitas_totales
    visitas_totales = 0
    print(f"Contador de visitas reseteado.")

vistas()
vistas()
vistas()


resteo()


vistas()
vistas()
