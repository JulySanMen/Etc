import math

def calcular_areas():
    print("Selecciona la forma para calcular el área:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Triángulo")
    print("5. Triángulo Isósceles")
    print("6. Triángulo Equilátero")
    
    opcion = int(input("Ingresa la opción: "))

    if opcion == 1:
        # Área de un Círculo: A = π * r^2
        radio = float(input("Ingresa el radio del círculo: "))
        area_circulo = math.pi * radio ** 2
        print(f"El área del círculo es: {area_circulo}")

    elif opcion == 2:
        # Área de un Cuadrado: A = lado^2
        lado = float(input("Ingresa el lado del cuadrado: "))
        area_cuadrado = lado ** 2
        print(f"El área del cuadrado es: {area_cuadrado}")

    elif opcion == 3:
        # Área de un Rectángulo: A = base * altura
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area_rectangulo = base * altura
        print(f"El área del rectángulo es: {area_rectangulo}")

    elif opcion == 4:
        # Área de un Triángulo: A = (base * altura) / 2
        base_tri = float(input("Ingresa la base del triángulo: "))
        altura_tri = float(input("Ingresa la altura del triángulo: "))
        area_triangulo = (base_tri * altura_tri) / 2
        print(f"El área del triángulo es: {area_triangulo}")

    elif opcion == 5:
        # Área de un Triángulo Isósceles
        base_iso = float(input("Ingresa la base del triángulo isósceles: "))
        lado_iso = float(input("Ingresa la longitud de los lados iguales del triángulo: "))
        
        # Calcular la altura usando Pitágoras
        altura_iso = math.sqrt(lado_iso ** 2 - (base_iso / 2) ** 2)
        area_isosceles = (base_iso * altura_iso) / 2
        print(f"El área del triángulo isósceles es: {area_isosceles}")

    elif opcion == 6:
        # Área de un Triángulo Equilátero: A = (sqrt(3) / 4) * l^2
        lado_equilatero = float(input("Ingresa la longitud de un lado del triángulo equilátero: "))
        area_equilatero = (math.sqrt(3) / 4) * lado_equilatero ** 2
        print(f"El área del triángulo equilátero es: {area_equilatero}")

    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    calcular_areas()
