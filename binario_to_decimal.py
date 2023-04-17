def binario_to_decimal(numero):
    n = len(numero) - 1
    resultado=0
    for i in numero:
        if i == "1":
            resultado += 2**n
        n -= 1 
    return resultado
            
            