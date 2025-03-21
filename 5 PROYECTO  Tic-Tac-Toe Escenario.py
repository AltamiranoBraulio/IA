from random import randrange

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    for i in range(3):
        if all([celda == jugador for celda in tablero[i]]):  # Filas
            return True
        if all([tablero[j][i] == jugador for j in range(3)]):  # Columnas
            return True
    if all([tablero[i][i] == jugador for i in range(3)]):  # Diagonal principal
        return True
    if all([tablero[i][2 - i] == jugador for i in range(3)]):  # Diagonal secundaria
        return True
    return False

# Función para verificar si el tablero está lleno (empate)
def tablero_lleno(tablero):
    return all([celda in ['X', 'O'] for fila in tablero for celda in fila])

# Función para el movimiento de la máquina
def movimiento_maquina(tablero):
    while True:
        movimiento = randrange(1, 10)  # Elige un número aleatorio del 1 al 9
        fila = (movimiento - 1) // 3
        columna = (movimiento - 1) % 3
        if tablero[fila][columna] not in ['X', 'O']:  # Verifica si la casilla está libre
            tablero[fila][columna] = 'X'
            break

# Función principal del juego
def tres_en_raya():
    # Inicializar el tablero
    tablero = [[str(i + 1 + j * 3) for i in range(3)] for j in range(3)]
    tablero[1][1] = 'X'  # La máquina siempre empieza en el centro

    mostrar_tablero(tablero)

    while True:
        # Turno del usuario
        try:
            movimiento = int(input("Ingresa tu movimiento (1-9): "))
            if movimiento < 1 or movimiento > 9:
                print("Número inválido. Intenta de nuevo.")
                continue
            fila = (movimiento - 1) // 3
            columna = (movimiento - 1) % 3
            if tablero[fila][columna] in ['X', 'O']:
                print("Casilla ocupada. Intenta de nuevo.")
                continue
            tablero[fila][columna] = 'O'
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
            continue

        mostrar_tablero(tablero)

        # Verificar si el usuario ganó
        if verificar_ganador(tablero, 'O'):
            print("¡Has Ganado!")
            break

        # Verificar si el tablero está lleno (empate)
        if tablero_lleno(tablero):
            print("¡Empate!")
            break

        # Turno de la máquina
        print("Turno de la máquina...")
        movimiento_maquina(tablero)
        mostrar_tablero(tablero)

        # Verificar si la máquina ganó
        if verificar_ganador(tablero, 'X'):
            print("¡La máquina ha ganado!")
            break

        # Verificar si el tablero está lleno (empate)
        if tablero_lleno(tablero):
            print("¡Empate!")
            break

# Iniciar el juego
tres_en_raya()