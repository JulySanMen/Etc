def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd}")
