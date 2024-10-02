def capitalizar_palabras(cadena):
    resultado = ""
    mayuscula_siguiente = True  # Bandera para saber cuándo poner una mayúscula
    
    for char in cadena:
        if mayuscula_siguiente and char.isalpha():  # Poner mayúscula si es una letra
            resultado += char.upper()  # Convertir a mayúscula
            mayuscula_siguiente = False  # No poner más mayúsculas hasta encontrar un espacio
        else:
            resultado += char  # Mantener el carácter tal como es
        
        if char == " ":
            mayuscula_siguiente = True
    
    return resultado

texto = input("Ingresa una frase o palabra: ")

resultado = capitalizar_palabras(texto)

print("Cadena capitalizada:", resultado)
