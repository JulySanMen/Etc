def conversion(n):
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

# Ejemplo
numero_decimal = 25
binario = conversion(numero_decimal)
print(f"El número {numero_decimal} en binario es: {binario}")


