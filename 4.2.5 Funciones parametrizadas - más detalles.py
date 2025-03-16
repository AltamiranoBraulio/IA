def cafe(tipo="americano", tamano="mediano", azucar=1, leche=false, extra=None ):
    descricion="preparando café {tipo} {tamano}"
    if leche:
        descricion+=" con leche"
    if extra:
        descricion+=" y "+extra
    descricion + f", con {azucar} cucharadas de azúcar"

    