# Calcularemos temperatura

def temperatura(celcius):
    kelvin = 273.15 + celcius
    farenheit = 9/5. * celcius + 32
    rankine = 9/5. * (celcius + 273.15)
    reaumur = 4/5. * celcius
    
    print(f"{celcius} grados Celsius valen:")
    print(f"{kelvin} grados Kelvin")
    print(f"{farenheit} grados Fahrenheit")
    print(f"{rankine} grados Rankine")
    print(f"{reaumur} grados Reaumur")

celcius = float(input("Ingrese temperatura en Celsius: "))
temperatura(celcius)
