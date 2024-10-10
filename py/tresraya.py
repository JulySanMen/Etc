def analizar_matriz(matriz):
    n = 3 
    contador_x = 0
    contador_o = 0

    for fila in matriz:
        contador_x += fila.count('X')
        contador_o += fila.count('O')

    if abs(contador_x - contador_o) > 1:
        return 'Nulo'
