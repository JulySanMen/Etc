def analizar_matriz(matriz):
    n = 3 


    contador_x = 0
    contador_o = 0

    for fila in matriz:
        contador_x += fila.count('X')
        contador_o += fila.count('O')

    if abs(contador_x - contador_o) > 1:
        return 'Nulo'


    def verificar_ganador(jugador):

        for i in range(n):
            if matriz[i][0] == jugador and matriz[i][1] == jugador and matriz[i][2] == jugador:
                return True

        for j in range(n):
            if matriz[0][j] == jugador and matriz[1][j] == jugador and matriz[2][j] == jugador:
                return True

        if matriz[0][0] == jugador and matriz[1][1] == jugador and matriz[2][2] == jugador:
            return True
        if matriz[0][2] == jugador and matriz[1][1] == jugador and matriz[2][0] == jugador:
            return True
        return False

    x_gana = verificar_ganador('X')
    o_gana = verificar_ganador('O')

    if x_gana and o_gana:
        return 'Nulo'
    if x_gana:
        return 'X'
    if o_gana:
        return 'O'
    
    hay_espacios_vacios = any('' in fila for fila in matriz)

    if not hay_espacios_vacios:
        return 'Empate'

    return 'En progreso'

matriz_ejemplo = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', '']
]

print(analizar_matriz(matriz_ejemplo))  
