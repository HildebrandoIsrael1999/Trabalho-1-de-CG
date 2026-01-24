from biblioteca import get_aabb, testa_colisao
from matrizes import calcularMatriz

class GerenciadorColisao:
    def __init__(self, lista_cenario):
        self.obstaculos = []

        for item in lista_cenario:
            m = calcularMatriz(1.0, 0, item["x"], item["y"])
            caixa = get_aabb(item["modelo"], m)
            self.obstaculos.append(caixa)

    def verificarMovimento(self, modelo, x, y, esc, ang):
        m_futura = calcularMatriz(esc, ang, x, y)
        caixa = get_aabb(modelo, m_futura)

        for obs in self.obstaculos:
            if testa_colisao(caixa, obs):
                return True 
        return False 