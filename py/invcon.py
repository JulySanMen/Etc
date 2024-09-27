def conversioninv(binario):
    decimal = 0
    potencia = 0

    while binario > 0:
        digito = binario % 10  
        decimal += digito * (2 ** potencia)
        binario //= 10  
        potencia += 1

    return decimal

numero_binario = int(input("Introduce un número binario: "))
numero_decimal = conversioninv(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {numero_decimal}")
