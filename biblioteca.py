import math
from matrizes import *
from clipping import *
CLIP_XMIN, CLIP_YMIN = 0, 0
CLIP_XMAX, CLIP_YMAX = 1280, 720

#Get usam para pegar os pontos para serem desenhados, assim facilitando ao utilizar as matrizes
#Set usam para desenhar na tela diretamente, pixel a pixel, dificilmente usável para personagens complexos, mas mais leves, ou seja, coisas estáticas.
def definirAreaDeRecorte(xmin, ymin, xmax, ymax):
    global CLIP_XMIN, CLIP_YMIN, CLIP_XMAX, CLIP_YMAX
    CLIP_XMIN, CLIP_YMIN = xmin, ymin
    CLIP_XMAX, CLIP_YMAX = xmax, ymax

def setPixel(superficie, x, y, cor):
    x = int(x)
    y = int(y)
    if CLIP_XMIN <= x < CLIP_XMAX and CLIP_YMIN <= y < CLIP_YMAX:
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

def setRetaRecortada(superficie, x0, y0, x1, y1, cor):

    resultado = cohenSutherlandClip(x0, y0, x1, y1, CLIP_XMIN, CLIP_YMIN, CLIP_XMAX, CLIP_YMAX)
    
    if resultado is None:
        return # Não desenha nada, economiza processamento.

    novo_x0, novo_y0, novo_x1, novo_y1 = resultado

    setRetaBresenham(superficie, novo_x0, novo_y0, novo_x1, novo_y1, cor)

def scanlineFill(superficie, pontos, cor_preenchimento):

    # Achar o topo e o fundo do desenho (Y mínimo e máximo)
    ys = [p[1] for p in pontos]
    y_min = int(min(ys))
    y_max = int(max(ys))

    n = len(pontos)

    # Descer linha por linha (da menor altura para a maior)
    for y in range(y_min, y_max):
        intersecoes_x = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n] # Conecta o último ponto ao primeiro

            if y0 == y1:
                continue


            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            if y < y0 or y >= y1:
                continue

            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes_x.append(x)

        intersecoes_x.sort()
        for i in range(0, len(intersecoes_x), 2):
            if i + 1 < len(intersecoes_x):
                x_inicio = int(round(intersecoes_x[i]))
                x_fim = int(round(intersecoes_x[i + 1]))

                # Desenha a linha horizontal pixel por pixel usando seu setPixel
                for x in range(x_inicio, x_fim + 1):
                    setPixel(superficie, x, y, cor_preenchimento)
                    
def scanlineTexture(superficie, pontos, uvs, textura):
    tex_w, tex_h = textura.get_width(), textura.get_height()
    n = len(pontos)
    ys = [p[1] for p in pontos]
    y_min, y_max = int(min(ys)), int(max(ys))

    for y in range(y_min, y_max):
        intersecoes = []
        for i in range(n):
            x0, y0 = pontos[i]; x1, y1 = pontos[(i + 1) % n]
            u0, v0 = uvs[i]; u1, v1 = uvs[(i + 1) % n]
            if y0 == y1: continue
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0
                u0, v0, u1, v1 = u1, v1, u0, v0
            if y < y0 or y >= y1: continue
            t = (y - y0) / (y1 - y0)
            intersecoes.append((x0 + t * (x1 - x0), u0 + t * (u1 - u0), v0 + t * (v1 - v0)))

        intersecoes.sort(key=lambda item: item[0])
        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_start, u_start, v_start = intersecoes[i]
                x_end, u_end, v_end = intersecoes[i+1]
                if int(x_start) == int(x_end): continue
                for x in range(int(x_start), int(x_end) + 1):
                    t_h = (x - x_start) / (x_end - x_start)
                    u = u_start + t_h * (u_end - u_start)
                    v = v_start + t_h * (v_end - v_start)
                    tx, ty = int(u * (tex_w - 1)), int(v * (tex_h - 1))
                    if 0 <= tx < tex_w and 0 <= ty < tex_h:
                        setPixel(superficie, x, y, textura.get_at((tx, ty)))
   
#mtodo de colorir usando scanline, porém com textura
def scanlineTexture(superficie, pontos, uvs, textura):
    # Pega as dimensões da imagem da textura
    tex_w, tex_h = textura.get_width(), textura.get_height()
    n = len(pontos)

    ys = [p[1] for p in pontos]
    y_min = int(min(ys))
    y_max = int(max(ys))

    for y in range(y_min, y_max):
        intersecoes = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]
            u0, v0 = uvs[i]
            u1, v1 = uvs[(i + 1) % n]

            if y0 == y1: continue

            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0
                u0, v0, u1, v1 = u1, v1, u0, v0

            if y < y0 or y >= y1: continue

            t = (y - y0) / (y1 - y0)
            
            x = x0 + t * (x1 - x0)
            u = u0 + t * (u1 - u0)
            v = v0 + t * (v1 - v0)
            intersecoes.append((x, u, v))

        intersecoes.sort(key=lambda item: item[0])

        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                x_inicio, u_inicio, v_inicio = intersecoes[i]
                x_fim, u_fim, v_fim = intersecoes[i+1]

                if int(x_inicio) == int(x_fim): continue

                for x in range(int(x_inicio), int(x_fim) + 1):
                    
                    t_horiz = (x - x_inicio) / (x_fim - x_inicio)
                    
                    u = u_inicio + t_horiz * (u_fim - u_inicio)
                    v = v_inicio + t_horiz * (v_fim - v_inicio)

                    tx = int(u * (tex_w - 1))
                    ty = int(v * (tex_h - 1))

                    if 0 <= tx < tex_w and 0 <= ty < tex_h:
                        cor = textura.get_at((tx, ty))
                        setPixel(superficie, x, y, cor)

def getRetanguloPreenchido(x, y, w, h, cor, nome="retangulo"):
    return {
        "nome": nome,
        "cor": cor,
        "pontos": [
            (x, y),          # Topo-Esq
            (x + w, y),      # Topo-Dir
            (x + w, y + h),  # Base-Dir
            (x, y + h)       # Base-Esq
        ]
    }

def getLinha(x1, y1, x2, y2, cor, nome="linha"):
    return {
        "nome": nome,
        "cor": cor,
        "tipo": "linha", # Já seta a flag automaticamente
        "pontos": [(x1, y1), (x2, y2)]
    }

def getQuadrado(x, y, w, h, cor, nome="contorno"):
    # Reaproveita a lógica do retângulo, mas seta o tipo
    obj = getRetanguloPreenchido(x, y, w, h, cor, nome)
    obj["tipo"] = "apenas_contorno"
    return obj  

def getRetangulo(x, y, w, h, cor, nome="contorno"):

    obj = getRetanguloPreenchido(x, y, w, h, cor, nome)
    obj["tipo"] = "apenas_contorno"
    return obj

def getCirculo(cx, cy, raio, cor, nome="circulo_vazado", resolucao=30):
    
    pontos = []
    passo_angulo = 360 / resolucao

    for i in range(resolucao):
        # Converte graus para radianos
        rad = math.radians(i * passo_angulo)
        # Calcula a posição do ponto na circunferência
        px = cx + raio * math.cos(rad)
        py = cy + raio * math.sin(rad)
        pontos.append((px, py))

    return {
        "nome": nome,
        "cor": cor,
        "tipo": "apenas_contorno", # Importante para ser vazado
        "pontos": pontos
    }
    
def getTrianguloPreenchido(p1, p2, p3, cor, nome="triangulo"):
    return {
        "nome": nome,
        "cor": cor,
        "pontos": [p1, p2, p3]
    }
                    
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
    # Calculamos a altura usando a fórmula
    altura = lado * (math.sqrt(3) / 2)
    
    # Definimos os três pontos (vértices)
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
    pontos = [
        (x, y), 
        (x + largura, y), 
        (x + largura, y + altura), 
        (x, y + altura)
    ]
    
    scanlineFill(superficie, pontos, cor)
     
def setPreencherQuadrado(superficie, x, y, tamanho, cor):
    pontos = [
        (x, y), 
        (x + tamanho, y), 
        (x + tamanho, y + tamanho), 
        (x, y + tamanho)
    ]
    
    #Chamamos a função de Scanline do professor para pintar o interior
    scanlineFill(superficie, pontos, cor)

def setPreencherTriangulo(superficie, x, y, lado, cor):
 
    # Calculamos a altura
    altura = lado * (math.sqrt(3) / 2)
    
    # Definimos os 3 cantos (vértices)
    # Ponto 1: Topo
    p1 = (x, y)
    # Ponto 2: Base Esquerda (anda metade do lado para a esquerda e desce a altura)
    p2 = (x - lado/2, y + altura)

    p3 = (x + lado/2, y + altura)
    
    pontos_triangulo = [p1, p2, p3]
    
    scanlineFill(superficie, pontos_triangulo, cor)
    
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
    pontos = [
        (x1, y1), 
        (x2, y2), 
        (x3, y3)
    ]
    
    scanlineFill(superficie, pontos, cor)
    
    
def renderizarPersonagem(superficie, modelo, matriz, textura_objeto=None):
    for parte in modelo:
        pts_trans = aplicaTransformacao(matriz, parte["pontos"])
        cor = parte["cor"]
        tipo = parte.get("tipo", "padrao")
        
        #logica de Preenchimento para textura ou cor solida
        if len(pts_trans) > 2 and tipo != "apenas_contorno" and tipo != "linha":
            # Se a parte tem UVs e recebemos uma textura, usa a função da sua amiga
            if "uvs" in parte and textura_objeto is not None:
                scanlineTexture(superficie, pts_trans, parte["uvs"], textura_objeto)
            else:
                scanlineFill(superficie, pts_trans, cor)
        
        # Bordas
        n = len(pts_trans)
        for i in range(n):
            if tipo == "linha" and i == n - 1: break
            p1, p2 = pts_trans[i], pts_trans[(i + 1) % n]
            setRetaRecortada(superficie, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), cor)
           
def desenhar_cenario(superficie, matriz_v=None, textura_bandeira=None):
    from cenarios import DADOS_DO_CENARIO, getBandeira
    if matriz_v is None: matriz_v = identidade()

    # Desenha a bandeira (que usa textura)
    m_band = calcularMatriz(1.0, 0, 100, 100)
    renderizarPersonagem(superficie, getBandeira(), multiplicaMatrizes(matriz_v, m_band), textura_bandeira)

    # Desenha o resto do cenário (cor sólida)
    for item in DADOS_DO_CENARIO:
        m_obj = calcularMatriz(1.0, 0, item["x"], item["y"])
        renderizarPersonagem(superficie, item["modelo"], multiplicaMatrizes(matriz_v, m_obj), None)

def renderizarViewport(superficie, matriz_vp, modelos_mundo, textura_grama=None):
    # Desenha a Moldura e o Fundo sólido
    setPreencherRetangulo(superficie, 958, 18, 304, 174, (0, 0, 0))    # Borda
    setPreencherRetangulo(superficie, 960, 20, 300, 170, (40, 40, 40)) # Fundo escuro

    definirAreaDeRecorte(960, 20, 1260, 190)
    
    # Desenha o Céu e Chão reduzidos
    setPreencherRetangulo(superficie, 960, 20, 300, 70, (146, 255, 222)) 
    setPreencherRetangulo(superficie, 960, 90, 300, 100, (100, 100, 100))

    # IMPORTANTE: Passar a textura para o desenho do cenário na viewport
    desenhar_cenario(superficie, matriz_vp, textura_grama)

    # Desenha os Personagens
    for modelo, matriz_original in modelos_mundo:
        m_final = multiplicaMatrizes(matriz_vp, matriz_original)
        renderizarPersonagem(superficie, modelo, m_final)
        
    # Reset do recorte
    definirAreaDeRecorte(0, 0, 1280, 720)
    
def limitar_personagem_na_janela(x, y, largura_obj, altura_obj, largura_janela, altura_janela):
    if x < 0:
        x = 0
    elif x + largura_obj > largura_janela:
        x = largura_janela - largura_obj

    if y < 0:
        y = 0
    elif y + altura_obj > altura_janela:
        y = altura_janela - altura_obj

    return x, y
 
