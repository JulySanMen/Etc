def diferencia_cadenas(str1, str2):
    
    out1 = ''.join([char for char in str1 if char not in str2])
    
    out2 = ''.join([char for char in str2 if char not in str1])
    

    print("Out1:", out1)
    print("Out2:", out2)
