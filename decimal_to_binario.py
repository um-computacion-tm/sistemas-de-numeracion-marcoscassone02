def decimal_to_binario(numero):
    resultado=""
    a = 0
    if numero == 0:
        resultado = "0"
    elif numero == 1:
        resultado = "1"
    else:
        while numero > 1:
            a = numero % 2
            a = str(a)
            resultado += a
            numero = int(numero / 2)
        if numero == 1:
            resultado += "1"
        elif numero == 0:
            resultado += "0"
    resultado = resultado[::-1]    
    return resultado
    