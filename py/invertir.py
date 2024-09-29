#def invertir_cadena(cadena):
 #   invertida = ""
  #  for i in range(len(cadena) - 1, -1, -1):
   #     invertida += cadena[i]
    #return invertida

#texto = "Hola mundo"
#resultado = invertir_cadena(texto)
#print(resultado)


def invertir(cadena):
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        invertida += cadena[i]
    return invertida
texto = input("Ingresa una frase o palabra: ")
resultado = invertir(texto)
print("Cadena invertida:", resultado)
