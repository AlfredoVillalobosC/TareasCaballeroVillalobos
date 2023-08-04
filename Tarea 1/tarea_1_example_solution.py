def separa_letras(cadena):  # inicia separa_letras cuya entrada es cadena
    codigo = 0  # salida de codigo de error
    mayus = None  # salida de string de mayusculas
    minus = None   # salida de string de minusculas
    if isinstance(cadena, str):      # se revisa si la entrada es una cadena
        if len(cadena) != 0:          # se revisa se la cadena esta vacia
            if cadena.isalpha():      # se revisa si es del abecedario
                mayus = ""              # mayus y minus como string vacio
                minus = ""
                for letra in cadena:    # mayus y minus a su respectivo string
                    if letra.isupper():
                        mayus = mayus+letra
                    else:
                        minus = minus+letra
            else:
                codigo = -200    # error si tiene un caracter no abecedario
        else:
            codigo = -300   # error si la cadena esta vacia
    else:
        codigo = -100           # error si la cadena es un numero
    return codigo, mayus, minus         # alida del codigo y strings


def potencia_manual(base, potencia):  # se define la funcion potencia_manual
    codigopot = 0               # salida codigo de error se asume 0
    total = None       # salida de la potencia

    if isinstance(base, str) or isinstance(potencia, str):
        codigopot = -400  # determina si entrada es string salida codigo error
    else:
        if potencia == 0:   # si la potencia es 0 el resultado es 1
            total = 1
        else:
            contador = base  # se coloca un contador para realizar las sumas
            total = base    # si potencia es 1 total es igual a base
        for i in range(1, potencia):   # desde 1 hasta potencia
            for j in range(1, base):     # desde 1 hasta base
                total += contador   # total se le suma contador
            contador = total   # contador cambia a total nuevo
    return codigopot, total
