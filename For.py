# Importar el módulo time para usar sleep()
import time

# Bucle for para contar de 1 a 5
for i in range(1,100):
    print(f"{i} Mississippi")  # Imprimir el número y "Mississippi"
    time.sleep(1)  # Esperar 1 segundo entre cada iteración

# Mensaje final
print("¡Listos o no, ahí voy!")