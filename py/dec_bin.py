def conversion(decimal):
    binario=""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario
decimal= int(input ("Introduce un numero en decimal: "))
binario=conversion(decimal)
print(f"El número {decimal} en binario es: {binario}")


# Ejemplo
#numero_decimal = 25
#binario = conversion(numero_decimal)



