import math

def calcular_distancia(coordenadas):
    x, y = coordenadas
    distancia = math.sqrt(x**2 + y**2)
    return distancia

punto =(8,3)


print(f"las coordenadas son: {punto}")

distancia_origen= calcular_distancia(punto)
print(f"la distancia al origen es: {distancia_origen} unidades")
  