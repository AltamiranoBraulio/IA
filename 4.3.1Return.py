def maquina (producto, dinero):
    precio=0
    if producto == refresco:
        cambio = dinero - 15
        return refresco, cambio
    else:
        if producto == papas:
            cambio = dinero - 10
            return papas, cambio
        else:
            if producto == chocolate:
                cambio = dinero - 12
                return chocolate, cambio
            else:
                if producto == galletas:
                    cambio = dinero - 8
                    return galletas, cambio
                else:
                    if producto == agua:
                        cambio = dinero - 7
                        return agua, cambio
                    else:
                        if producto == chicles:
                            cambio = dinero - 5
                            return chicles, cambio
                        else:
                            return "Producto no disponible"



