simbolos = {
    1 : "I",
    5 : "V"
}

def entero_a_romano(n_int):
    if n_int in simbolos:
        return simbolos[n_int]
    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4:
        return simbolos[1] + simbolos[5]
    else:
        multiplicador = n_int - 5
        return simbolos[5] + multiplicador * simbolos[1]

if __name__ == "__main__": #Esto es para que solo ejecute el codigo que sigue cuando ejecutemos el programa desde romannumbers, pero en otros ficheros donde se importe no se va a ejecutar
    print(entero_a_romano(6))