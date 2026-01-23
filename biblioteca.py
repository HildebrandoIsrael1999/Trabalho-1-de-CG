import math
from matrizes import *
from cenarios import *

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
    
def setTrianguloGenerico(superficie, x1, y1, x2, y2, x3, y3, cor):
    # Desenha a linha entre cada par de pontos fornecidos
    setRetaBresenham(superficie, x1, y1, x2, y2, cor) # Lado A
    setRetaBresenham(superficie, x2, y2, x3, y3, cor) # Lado B
    setRetaBresenham(superficie, x3, y3, x1, y1, cor) # Lado C

def setPreencherTrianguloGenerico(superficie, x1, y1, x2, y2, x3, y3, cor):
    # 1. Criamos a lista com os 3 vértices do triângulo
    # Diferente do retângulo, a ordem dos pontos aqui não costuma afetar o scanline
    pontos = [
        (x1, y1), 
        (x2, y2), 
        (x3, y3)
    ]
    
    # 2. Chamamos a função scanline_fill enviando a lista de 3 pontos
    scanline_fill(superficie, pontos, cor)
    
def renderizarPersonagem(superficie, modelo, matriz):
    for parte in modelo:
        # Aplica a matriz composta (Escala, Rotação, Translação)
        pts_trans = aplicaTransformacao(matriz, parte["pontos"])
        cor = parte["cor"]
        
        # Só preenche se não for uma peça marcada como 'apenas_contorno' ou 'linha'
        if len(pts_trans) > 2 and parte.get("tipo") != "apenas_contorno" and parte.get("tipo") != "linha":
            scanline_fill(superficie, pts_trans, cor)
        
        # Desenha o contorno com a mesma cor para suavizar as bordas e nao ficar com aquele treco preto ao redor
        n = len(pts_trans)
        for i in range(n):
            # Se for 'linha', não fecha o polígono (ex: boca) OBS:hidelbrando não apaga para nao deformar a boca do billy
            if parte.get("tipo") == "linha" and i == n - 1:
                break
                
            p1 = pts_trans[i]
            p2 = pts_trans[(i + 1) % n]
            
            setRetaBresenham(superficie, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), cor)
            
def desenhar_cenario(superficie, matriz_v=None):
    # Se não passarmos matriz, usamos a identidade (desenha no tamanho real)
    if matriz_v is None:
        matriz_v = identidade()

    def posicionar_e_desenhar(modelo, x, y):
        # 1. Matriz de posição no mundo
        m_obj = calcularMatriz(1.0, 0, x, y)
        # 2. Composição: multiplica a posição do objeto pela matriz da viewport(Verificar)
        m_final = multiplicaMatrizes(matriz_v,m_obj)
        renderizarPersonagem(superficie, modelo, m_final)

    # Chamadas originais (elas agora serão afetadas pela matriz_v)
    posicionar_e_desenhar(getMoita(), 420, 260)
    posicionar_e_desenhar(getCarrinho(), 100, 350)
    posicionar_e_desenhar(getJarro(), 30, 290)
    posicionar_e_desenhar(getBanco(), 700, 300)
    posicionar_e_desenhar(getCachorro(), 500, 400)
    posicionar_e_desenhar(getCachorro(marrom=True), 700, 600)
    posicionar_e_desenhar(getCarro(), 1073, 400)
    posicionar_e_desenhar(getLixeiras(), 1050, 250)
    posicionar_e_desenhar(getGato(), 800, 500)

def renderizarViewport(superficie, matriz_vp, modelos_mundo):
    # 1. Desenha a Moldura e o Fundo sólido
    setPreencherRetangulo(superficie, 958, 18, 304, 174, (0, 0, 0))    # Borda
    setPreencherRetangulo(superficie, 960, 20, 300, 170, (40, 40, 40)) # Fundo escuro

    # 2. Desenha o CÉU e CHÃO reduzidos (Truque visual)
    # Céu reduzido (proporcional aos 300px de altura da tela original)
    setPreencherRetangulo(superficie, 960, 20, 300, 70, (146, 255, 222)) 
    # Chão reduzido (proporcional aos 450px de altura da tela original)
    setPreencherRetangulo(superficie, 960, 90, 300, 100, (100, 100, 100))

    # 3. Desenha o Cenário (passando a matriz da viewport)
    desenhar_cenario(superficie, matriz_vp)

    # 4. Desenha os Personagens
    for modelo, matriz_original in modelos_mundo:
        m_final = multiplicaMatrizes(matriz_vp, matriz_original)
        renderizarPersonagem(superficie, modelo, m_final)