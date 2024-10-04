def cadenas():
    
    str1 = input("Ingresa la primera cadena: ")
    str2 = input("Ingresa la segunda cadena: ")
    
    out1 = ''.join([char for char in str1 if char not in str2])
    out2 = ''.join([char for char in str2 if char not in str1])
    
    print("Out1:", out1)
    print("Out2:", out2)

cadenas()
