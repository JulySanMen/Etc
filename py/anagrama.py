def anagramas(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    return sorted(palabra1) == sorted(palabra2)

print(anagramas("amor", "roma")) 
print(anagramas("amor", "amora")) 
print(anagramas("amor", "amor"))  