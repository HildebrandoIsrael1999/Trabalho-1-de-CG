import math

def setPixel(superficie, x, y, cor):
    x = int(x)
    y = int(y)
    #If para garantir que ele não pinte um pixel fora da tela
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)

def setRetaBresenham(superficie, x0, y0, x1, y1, cor):
  # Flags para transformações
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    ystep = 1
    if dy < 0:
        ystep = -1
        dy = -dy

    # Bresenham clássico
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x0
    y = y0

    while x <= x1:
        if steep:
            setPixel(superficie, y, x, cor)
        else:
            setPixel(superficie, x, y, cor)

        if d <= 0:
            d += incE
        else:
            d += incNE
            y += ystep

        x += 1

def scanline_fill(superficie, pontos, cor_preenchimento):
    """
    Pinta o interior de uma forma (como um quadrado ou triângulo).
    'pontos' é uma lista de coordenadas [(x1, y1), (x2, y2), ...]
    """
    # 1. Achar o topo e o fundo do desenho (Y mínimo e máximo)
    ys = [p[1] for p in pontos]
    y_min = int(min(ys))
    y_max = int(max(ys))

    n = len(pontos)

    # 2. Descer linha por linha (da menor altura para a maior)
    for y in range(y_min, y_max):
        intersecoes_x = []

        # 3. Para cada lado (aresta) do desenho, ver se a linha 'y' corta ele
        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n] # Conecta o último ponto ao primeiro

            # Ignora se a linha for perfeitamente horizontal (não tem o que calcular)
            if y0 == y1:
                continue

            # Garante que estamos olhando de cima para baixo
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            # Verifica se a linha horizontal 'y' está passando por esse lado
            if y < y0 or y >= y1:
                continue

            # Descobre o X exato onde a linha encosta na parede
            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes_x.append(x)

        # 4. Coloca os pontos encontrados em ordem da esquerda para a direita
        intersecoes_x.sort()

        # 5. Pinta sempre o espaço entre os pares de paredes encontrados
        for i in range(0, len(intersecoes_x), 2):
            if i + 1 < len(intersecoes_x):
                x_inicio = int(round(intersecoes_x[i]))
                x_fim = int(round(intersecoes_x[i + 1]))

                # Desenha a linha horizontal pixel por pixel usando seu setPixel
                for x in range(x_inicio, x_fim + 1):
                    setPixel(superficie, x, y, cor_preenchimento)
                    
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
    """
    Usa a função scanline_fill do professor para preencher um retângulo.
    """
    # 1. Criamos a lista com os 4 cantos do retângulo (em ordem)
    # Ponto 1: Topo-Esquerda
    # Ponto 2: Topo-Direita
    # Ponto 3: Base-Direita
    # Ponto 4: Base-Esquerda
    pontos = [
        (x, y), 
        (x + largura, y), 
        (x + largura, y + altura), 
        (x, y + altura)
    ]
    
    # 2. Chamamos a função do professor enviando essa lista
    scanline_fill(superficie, pontos, cor)
     
def setPreencherQuadrado(superficie, x, y, tamanho, cor):
    # 1. Definimos os 4 cantos do quadrado em ordem (seguindo o contorno)
    # Ponto 1: Topo-Esquerda (x, y)
    # Ponto 2: Topo-Direita  (x + tamanho, y)
    # Ponto 3: Base-Direita  (x + tamanho, y + tamanho)
    # Ponto 4: Base-Esquerda (x, y + tamanho)
    pontos = [
        (x, y), 
        (x + tamanho, y), 
        (x + tamanho, y + tamanho), 
        (x, y + tamanho)
    ]
    
    # 2. Chamamos a função de Scanline do professor para pintar o interior
    scanline_fill(superficie, pontos, cor)


def setPreencherTriangulo(superficie, x, y, lado, cor):
 
    # 1. Calculamos a altura (H = Lado * 0.866)
    altura = lado * (math.sqrt(3) / 2)
    
    # 2. Definimos os 3 cantos (vértices)
    # Ponto 1: Topo
    p1 = (x, y)
    # Ponto 2: Base Esquerda (anda metade do lado para a esquerda e desce a altura)
    p2 = (x - lado/2, y + altura)
    # Ponto 3: Base Direita (anda metade do lado para a direita e desce a altura)
    p3 = (x + lado/2, y + altura)
    
    # 3. Colocamos os pontos em uma lista
    pontos_triangulo = [p1, p2, p3]
    
    # 4. Chamamos a função do professor para "escaneá-lo" e pintá-lo
    scanline_fill(superficie, pontos_triangulo, cor)
    
def setCirculo(superficie, centro_x, centro_y, raio, cor):
    x = 0
    y = raio
    d = 3 - 2 * raio

    plotarSimetriaCirculo(superficie, centro_x, centro_y, x, y, cor)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        plotarSimetriaCirculo(superficie, centro_x, centro_y, x, y, cor)

def plotarSimetriaCirculo(superficie, cx, cy, x, y, cor):
    setPixel(superficie, cx + x, cy + y, cor)
    setPixel(superficie, cx - x, cy + y, cor)
    setPixel(superficie, cx + x, cy - y, cor)
    setPixel(superficie, cx - x, cy - y, cor)
    setPixel(superficie, cx + y, cy + x, cor)
    setPixel(superficie, cx - y, cy + x, cor)
    setPixel(superficie, cx + y, cy - x, cor)
    setPixel(superficie, cx - y, cy - x, cor)