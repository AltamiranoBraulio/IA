# Programa para jugar al Tres en Raya (Tic-Tac-Toe) usando un arreglo de dos dimensiones

# Crear un tablero de 3x3 vacío
board = [
    [" ", " ", " "],  # Fila 1
    [" ", " ", " "],  # Fila 2
    [" ", " ", " "]   # Fila 3
]

# Función para imprimir el tablero
def print_board():
    print("\nTablero actual:")
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Función para verificar si hay un ganador
def check_winner():
    # Verificar filas
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Verificar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Función para verificar si el tablero está lleno (empate)
def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

# Inicializar el juego
current_player = "X"
print("¡Bienvenidos al Tres en Raya!")
print_board()

# Ciclo principal del juego
while True:
    # Pedir al jugador actual que ingrese su movimiento
    print(f"Turno del jugador {current_player}")
    try:
        row = int(input("Ingresa el número de fila (0, 1, 2): "))
        col = int(input("Ingresa el número de columna (0, 1, 2): "))

        # Verificar si la casilla está vacía
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board()

            # Verificar si hay un ganador
            if check_winner():
                print(f"¡Felicidades! El jugador {current_player} ha ganado.")
                break

            # Verificar si el tablero está lleno (empate)
            if is_board_full():
                print("¡Es un empate!")
                break

            # Cambiar al siguiente jugador
            current_player = "O" if current_player == "X" else "X"
        else:
            print("¡Casilla ocupada! Intenta de nuevo.")
    except (ValueError, IndexError):
        print("¡Entrada inválida! Ingresa números entre 0 y 2.")