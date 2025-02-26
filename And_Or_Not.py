# Solicitar al usuario que ingrese su edad y si tiene licencia de conducir
edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("¿Tienes licencia de conducir? (sí/no): ").lower()

# Verificar si el usuario puede conducir legalmente
if edad >= 18 and tiene_licencia == "sí":
    print("Puedes conducir legalmente.")
elif edad >= 18 and tiene_licencia == "no":
    print("Eres mayor de edad, pero necesitas una licencia para conducir.")
elif edad < 18 and tiene_licencia == "sí":
    print("No puedes conducir legalmente, aunque tengas licencia.")
else:
    print("No puedes conducir legalmente.")

# Verificar si el usuario es joven o no tiene licencia
if edad < 25 or tiene_licencia == "no":
    print("Eres joven o no tienes licencia.")

# Verificar si el usuario no puede conducir
if not (edad >= 18 and tiene_licencia == "sí"):
    print("No cumples con los requisitos para conducir legalmente.")