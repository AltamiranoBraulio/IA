# Solicitar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Variable para almacenar la palabra sin vocales
word_without_vowels = ""

# Bucle for para iterar sobre cada letra de la palabra
for letra in user_word:
    # Verificar si la letra es una vocal
    if letra in "AEIOU":
        continue  # Omitir las vocales
    # Concatenar las consonantes a word_without_vowels
    word_without_vowels += letra

# Imprimir la palabra sin vocales
print(word_without_vowels)