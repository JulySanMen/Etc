def invertir_cadena(cadena):
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        invertida += cadena[i]
    return invertida

texto = "Hola mundo"
resultado = invertir_cadena(texto)
print(resultado)
