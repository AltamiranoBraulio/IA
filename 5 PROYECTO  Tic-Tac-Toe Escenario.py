from random import randrange
def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
def verificar_ganador(tablero, jugador):
    for i in range(3):
        if all([celda == jugador for celda in tablero[i]]):  # Filas
            return True
        if all([tablero[j][i] == jugador for j in range(3)]):  # Columnas
            return True
    if all([tablero[i][i] == jugador for i in range(3)]):  # Diagonal principal
        return True
    