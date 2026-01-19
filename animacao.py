from biblioteca import setTrianguloEquilatero

class TrianguloAnimado:
    def __init__(self, x, y, tamanho, cor, velocidade):
        
        # Inicializa o triângulo com posição, tamanho, cor e velocidade.
        
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.cor = cor
        self.velocidade = velocidade

    def atualizar(self):
        
        # Atualiza a lógica (matemática) da posição.
        # Move o triângulo para a direita.
        
        self.x += self.velocidade

        # Opcional: Se passar da largura (1280), volta para o início (loop)
        if self.x > 1280:
            self.x = -self.tamanho

    def desenhar(self, tela):
        
        # Chama a função da sua biblioteca para desenhar na tela.
        
        # Passamos self.x e self.y que foram alterados no método atualizar()
        setTrianguloEquilatero(tela, self.x, self.y, self.tamanho, self.cor)