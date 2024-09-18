def son_anagramas(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    return sorted(palabra1) == sorted(palabra2)

print(son_anagramas("amor", "roma")) 
print(son_anagramas("amor", "amora")) 
print(son_anagramas("amor", "amor"))  