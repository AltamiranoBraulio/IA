# Solicitar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Bucle for para iterar sobre cada letra de la palabra
for letra in user_word:
    # Verificar si la letra es una vocal
    if letra in "AEIOU":
        continue  # Omitir las vocales
    # Imprimir las consonantes
    print(letra)