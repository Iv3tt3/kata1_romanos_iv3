unidades = {
    1 : "I",
    5 : "V",
    10: "X"
}
decenas = {
    1 : "X",
    5 : "L",
    10: "C"
}

centenas = {
    1: "C",
    5: "D",
    10: "M"
}

miles = {
    1: "M"
}

class RomanNumberError(Exception):
    pass

def listar_numero(num):
    n_mil = num // 1000 * 1000
    n_cent = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10)

    return n_mil, n_cent, n_dec, n_uni

def sacar_clave(num):
    if num >=1000:
        clave = miles
        num = num // 1000
    
    elif num >= 100:
        clave = centenas
        num = num // 100

    elif num >= 10:
        clave = decenas
        num = num // 10
    else: 
        clave = unidades
    return clave, num

def sacar_simbolo_digito(clau, digit):
    simbol_digit = ""
    if digit < 4:
        simbol_digit += digit * clau[1]
    elif digit == 4:
        simbol_digit += clau[1] + clau[5]
    elif digit < 9:
        num_unidades = digit - 5
        simbol_digit += clau[5] + num_unidades * clau[1]
    else:
        simbol_digit += clau[1] + clau[10]
    return simbol_digit 


def entero_a_romano(n_int):
    if n_int > 3999:
        raise RomanNumberError("RomanNumber must be less of 4000")
    
    digitos = listar_numero(n_int)

    resultado = ''

    for digito in digitos:
        if digito == 0:
            continue # te ignora el siguiente codigo del for y te coge el siguiente digito
        
        clave, digito = sacar_clave(digito)

        resultado += sacar_simbolo_digito(clave, digito)

    return resultado

if __name__ == "__main__": #Esto es para que solo ejecute el codigo que sigue cuando ejecutemos el programa desde romannumbers, pero en otros ficheros donde se importe no se va a ejecutar
    print(entero_a_romano(0))