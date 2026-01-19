import math

def setPixel(superficie, x, y, cor):
    x = int(x)
    y = int(y)
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)

def setRetaBresenham(superficie, x0, y0, x1, y1, cor):
    
    # Verifica se a linha está mais "em pé" do que "deitada"
    steep = abs(y1 - y0) > abs(x1 - x0)
    
    # Se a linha for íngreme, o código inverte X e Y. Isso transforma a linha "em pé" numa linha "deitada" para facilitar o cálculo.
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    
    # Deltas (Calculam a distância total que a linha percorre nos eixos)
    dx = x1 - x0
    dy = y1 - y0

    # Define se a linha está subindo ou descendo
    ystep = 1
    if dy < 0:
        ystep = -1
        dy = -dy

    # Bresenham clássico
    # É uma variável de erro acumulado. Ela diz ao algoritmo quão longe o pixel atual está da linha matemática "ideal"
    d = 2 * dy - dx
    # apenas andamos em X
    incE = 2 * dy
    # andamos em X e em Y
    incNE = 2 * (dy - dx)

    x = x0
    y = y0

    # 
    while x <= x1:
        
        # Se steep for True, as variáveis locais x e y do loop estão invertidas em relação à tela real. Por isso passamos (y, x) para a função setPixel.
        if steep:
            setPixel(superficie, y, x, cor)
        # Se steep for False, pintamos normalmente (x, y).
        else:
            setPixel(superficie, x, y, cor)

        if d <= 0:
            d += incE # Escolhe pixel E (East/Leste)
        else:
            d += incNE # Escolhe pixel NE (North-East/Nordeste)
            y += ystep

        x += 1

def setQuadrado(superficie, x, y, tamanho, cor):
    # 1. Linha do Topo (da esquerda para a direita)
    setRetaBresenham(superficie, x, y, x + tamanho, y, cor)
    
    # 2. Linha da Esquerda (de cima para baixo)
    setRetaBresenham(superficie, x, y, x, y + tamanho, cor)
    
    # 3. Linha da Direita (de cima para baixo, deslocada pelo tamanho)
    setRetaBresenham(superficie, x + tamanho, y, x + tamanho, y + tamanho, cor)

    # 4. Linha de Baixo (da esquerda para a direita, deslocada para baixo)
    setRetaBresenham(superficie, x, y + tamanho, x + tamanho, y + tamanho, cor)
    
def setRetangulo(superficie, x, y, largura, altura, cor):
    
    # 1. Linha do Topo (da esquerda para a direita)
    setRetaBresenham(superficie, x, y, x + largura, y, cor)
    
    # 2. Linha da Esquerda (de cima para baixo)
    setRetaBresenham(superficie, x, y, x, y + altura, cor)
    
    # 3. Linha da Direita (de cima para baixo, deslocada pelo tamanho)
    setRetaBresenham(superficie, x + largura, y, x + largura, y + altura, cor)
    
    # 4. Linha de baixo (da esquerda para a direita, deslocada para baixo)
    setRetaBresenham(superficie, x, y + altura, x + largura, y + altura,cor)
    
def setTrianguloEquilatero(superficie, x, y, lado, cor):
    # 1. Calculamos a altura usando a fórmula
    altura = lado * (math.sqrt(3) / 2)
    
    # 2. Definimos os três pontos (vértices)
    # Ponto 1: Topo (o x, y que passamos)
    p1x, p1y = x, y
    
    # Ponto 2: Inferior Esquerdo
    p2x, p2y = x - (lado / 2), y + altura
    
    # Ponto 3: Inferior Direito
    p3x, p3y = x + (lado / 2), y + altura
    
    # 3. Desenhamos as 3 linhas para fechar o triângulo
    setRetaBresenham(superficie, p1x, p1y, p2x, p2y, cor) # Lado esquerdo
    setRetaBresenham(superficie, p1x, p1y, p3x, p3y, cor) # Lado direito
    setRetaBresenham(superficie, p2x, p2y, p3x, p3y, cor) # Base
    
def setPreencherRetangulo(superficie, x, y, largura, altura, cor):
    
    
    # 1. O primeiro loop percorre a ALTURA (linha por linha)
    for linha in range(altura):
        
        # 2. O segundo loop percorre a LARGURA (pixel por pixel daquela linha)
        for coluna in range(largura):
            
            # Calculamos a posição exata do pixel atual
            pixel_x = x + coluna
            pixel_y = y + linha
            
            # Pintamos o pixel usando sua função base
            setPixel(superficie, pixel_x, pixel_y, cor)
def setPreencherTriangulo(superficie, x, y, lado, cor):
    # 1. Calculamos a altura (como fizemos antes)
    altura = int(lado * (math.sqrt(3) / 2))
    
    # 2. Vamos descer linha por linha (da ponta para a base)
    for i in range(altura + 1):
        # O 'i' representa a linha atual onde estamos pintando.
        # Em cada linha, a largura da "fatia" aumenta.
        
        # Proporção: quanto mais eu desço, mais largo fica
        largura_na_linha = (i / altura) * lado
        
        # O ponto inicial (esquerda) e final (direita) da linha horizontal
        x_esquerda = x - (largura_na_linha / 2)
        x_direita = x + (largura_na_linha / 2)
        
        # A altura atual (y original + quanto já descemos)
        y_atual = y + i
        
        # 3. Desenha uma linha horizontal preenchendo o espaço
        setRetaBresenham(superficie, int(x_esquerda), y_atual, int(x_direita), y_atual, cor)
