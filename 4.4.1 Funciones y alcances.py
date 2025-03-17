puntaje_total = 0

def jugar():
    puntaje_local =0

    print("bienvenido al juego")



    for i in range(3):
        puntaje_local += 10
        print(f"ganas diez puntos. puntaje local: {puntaje_local}")

    global puntaje_total
    puntaje_total += puntaje_local
    print(f"puntaje tota hasta ahora: {puntaje_total}")


def fin_del_juego():
    print(f"puntaje total: {puntaje_total}")


jugar()
jugar()
fin_del_juego()
