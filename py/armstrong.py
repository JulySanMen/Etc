#Un número de Armstrong (o número narcisista) es un número que es igual a la suma de sus propios dígitos 
#elevados a la potencia del número de dígitos. 
#Por ejemplo, el número 153 es un número de Armstrong, ya que: 1^3+5^3+3^3 = 153

def num_armstrong(numero):
    # Convertimos el número a una cadena para contar los dígitos
    digitos = str(numero)
    n = len(digitos) 

    # Calculamos la suma de los dígitos elevados a la potencia de n
    suma = sum(int(digito) ** n for digito in digitos)

    # Verificamos si la suma es igual al número original
    return suma == numero

numero = int(input("Ingresa un número: "))

if num_armstrong(numero):
    print(f"{numero} es un número de Armstrong.")
else:
    print(f"{numero} no es un número de Armstrong.")
