import math 

def identidade():
    return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def translacao(tx, ty):
    return [[1, 0, tx], [0, 1, ty], [0, 0, 1]]

def escala(sx, sy):
    return [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

def rotacao(angulo_graus):
    # Converte graus para radianos conforme a fórmula dos slides do Matheus
    theta = math.radians(angulo_graus)
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]

def multiplica_matrizes(a, b):
    r = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += a[i][k] * b[k][j]
    return r

def aplica_transformacao(m, pontos):
    novos = []
    for x, y in pontos:
        # v = [x, y, 1] em coordenadas homogêneas para translação
        nx = m[0][0]*x + m[0][1]*y + m[0][2]
        ny = m[1][0]*x + m[1][1]*y + m[1][2]
        novos.append((nx, ny))
    return novos