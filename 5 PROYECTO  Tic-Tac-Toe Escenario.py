from random import randrange
def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
