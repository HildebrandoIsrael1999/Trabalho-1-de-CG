import math
from matrizes import calcularMatriz

# --- CONFIGURAÇÕES DE POSIÇÃO ---
# Posição do queijo na mesa (carrinho)
X_MESA, Y_MESA = 210, 385 
# Posição da tapioca da frente (onde vamos colocar o queijo)
X_TAPIOCA, Y_TAPIOCA = 173, 380

# --- FUNÇÕES DE LÓGICA (DISTÂNCIA) ---

def pode_pegar_queijo(billy_x, billy_y):
    """ Verifica se o Billy está perto do carrinho para pegar o queijo """
    # Tolerância de 100px para facilitar a jogabilidade
    distancia = math.hypot(billy_x - X_MESA, billy_y - Y_MESA)
    return distancia < 100

def pode_colocar_queijo(billy_x, billy_y):
    """ Verifica se o Billy está perto da tapioca para soltar o queijo """
    distancia = math.hypot(billy_x - X_TAPIOCA, billy_y - Y_TAPIOCA)
    return distancia < 150

# --- FUNÇÕES DE MATRIZES (ONDE DESENHAR) ---

def get_matriz_queijo_mesa():
    """ Retorna a matriz do queijo parado na mesa """
    return calcularMatriz(1.0, 0, X_MESA, Y_MESA)

def get_matriz_queijo_mao(billy_x, billy_y):
    """ Retorna a matriz do queijo na mão do Billy (seguindo ele) """
    # Ajustes: +30 (lado) e +60 (altura da mão/cintura)
    offset_x = 30
    offset_y = 60
    # Escala 0.7 para ficar menorzinho
    return calcularMatriz(0.7, 0, billy_x + offset_x, billy_y + offset_y)

def get_matriz_queijo_tapioca():
    X_TAPIOCA, Y_TAPIOCA = 162, 374
    return calcularMatriz(1.0, 0, X_TAPIOCA, Y_TAPIOCA)