import math 

def identidade():
    return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def translacao(tx, ty):
    return [[1, 0, tx], [0, 1, ty], [0, 0, 1]]

def escala(sx, sy):
    return [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

def rotacao(angulo_graus):
    
    theta = math.radians(angulo_graus)
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]

def multiplicaMatrizes(a, b):
    r = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += a[i][k] * b[k][j]
    return r

def aplicaTransformacao(m, pontos):
    novos = []
    for x, y in pontos:
        
        nx = m[0][0]*x + m[0][1]*y + m[0][2]
        ny = m[1][0]*x + m[1][1]*y + m[1][2]
        novos.append((nx, ny))
    return novos

def calcularMatriz(esc, ang, x, y):
    m = identidade()
    m = multiplicaMatrizes(escala(esc, esc), m)
    m = multiplicaMatrizes(rotacao(ang), m)
    m = multiplicaMatrizes(translacao(x, y), m)
    return m

def calcularMatrizViewport(v_xmin, v_ymin, v_xmax, v_ymax, largura_mundo=1280, altura_mundo=720):

    sx = (v_xmax - v_xmin) / largura_mundo
    sy = (v_ymax - v_ymin) / altura_mundo

    m = identidade()
    m = multiplicaMatrizes(escala(sx, sy), m)
    m = multiplicaMatrizes(translacao(v_xmin, v_ymin), m)
    
    return m

def get_aabb(modelo, matriz):
    todos_pontos_transformados = []
    
    for parte in modelo:
        pts = aplicaTransformacao(matriz, parte["pontos"])
        todos_pontos_transformados.extend(pts)

    if not todos_pontos_transformados:
        return 0, 0, 0, 0

    x_coords = [p[0] for p in todos_pontos_transformados]
    y_coords = [p[1] for p in todos_pontos_transformados]
    
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    
    return {
        'x': x_min,
        'y': y_min,
        'w': x_max - x_min,
        'h': y_max - y_min
    }
def testa_colisao(aabb1, aabb2):
    return (aabb1['x'] < aabb2['x'] + aabb2['w'] and
            aabb1['x'] + aabb1['w'] > aabb2['x'] and
            aabb1['y'] < aabb2['y'] + aabb2['h'] and
            aabb1['y'] + aabb1['h'] > aabb2['y'])