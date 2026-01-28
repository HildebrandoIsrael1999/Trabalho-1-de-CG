import math
from matrizes import calcularMatriz
from textos import *


X_CAIXA, Y_CAIXA = 980, 480
X_TAPIOCA, Y_TAPIOCA = 173, 380
billy_pegou_queijo = False


def pode_pegar_queijo(billy_x, billy_y):
    distancia = math.hypot(billy_x - X_CAIXA, billy_y - Y_CAIXA)

    return distancia < 100

def pode_colocar_queijo(billy_x, billy_y):
    distancia = math.hypot(billy_x - X_TAPIOCA, billy_y - Y_TAPIOCA)
    return distancia < 150

def pode_entregar_tapioca(billy_x, billy_y, clara_x, clara_y):
    distancia = math.hypot(billy_x - clara_x, billy_y - clara_y)
    
    return distancia < 400 

def get_matriz_queijo_mesa():
    return calcularMatriz(1.0, 0, X_CAIXA, Y_CAIXA)

def get_matriz_queijo_mao(billy_x, billy_y):
    offset_x = 30
    offset_y = 60
    return calcularMatriz(0.7, 0, billy_x + offset_x, billy_y + offset_y)

def get_matriz_queijo_tapioca():
    ajuste_x = -10
    ajuste_y = -5 
    return calcularMatriz(1.0, 0, X_TAPIOCA + ajuste_x, Y_TAPIOCA + ajuste_y)


def get_matriz_queijo_clara(clara_x, clara_y):
    
    offset_x = 20
    offset_y = 50 
    return calcularMatriz(0.7, 0, clara_x + offset_x, clara_y + offset_y)

def get_matriz_tapioca_mesa():
    
    return calcularMatriz(1.0, 0, X_TAPIOCA, Y_TAPIOCA)

def get_matriz_tapioca_clara(clara_x, clara_y):
    
    offset_x = 30
    offset_y = 55 
    return calcularMatriz(0.7, 0, clara_x + offset_x, clara_y + offset_y)

def mover_npc_para_alvo(x_atual, y_atual, x_alvo, y_alvo, velocidade):

    dx = x_alvo - x_atual
    dy = y_alvo - y_atual
    distancia = math.hypot(dx, dy)


    if distancia < velocidade:
        return x_alvo, y_alvo, True

    move_x = (dx / distancia) * velocidade
    move_y = (dy / distancia) * velocidade

    return x_atual + move_x, y_atual + move_y, False