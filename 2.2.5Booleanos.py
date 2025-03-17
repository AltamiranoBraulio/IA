# Definimos valores booleanos
es_mayor_de_edad = True
tiene_permiso = False

# Imprimimos los valores directamente
print("¿Es mayor de edad?", es_mayor_de_edad)
print("¿Tiene permiso?", tiene_permiso)

# Usamos operadores lógicos con print
print("¿Puede entrar a la fiesta?", es_mayor_de_edad or tiene_permiso)
print("¿Está completamente autorizado?", es_mayor_de_edad and tiene_permiso)
print("¿No tiene permiso?", not tiene_permiso)
