def conversioninv(binario):
    decimal = 0
    potencia = 0

    while binario > 0:
        digito = binario % 10  # Obtener el último dígito del número binario
        decimal += digito * (2 ** potencia)
        binario //= 10  # Eliminar el último dígito del número binario
        potencia += 1

    return decimal

# Programa principal
numero_binario = int(input("Introduce un número binario: "))
numero_decimal = conversioninv(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {numero_decimal}")
