# Solicitar la entrada al usuario
entrada = input("Ingresa el nombre de la planta: ")

# Comparar la entrada y mostrar el mensaje correspondiente
if entrada == "ESPATIFILIO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print(f"¡Espatifilo!, ¡No {entrada}!")