import pygame
from biblioteca import *

if not pygame.font.get_init():
    pygame.font.init()

FONTE_PADRAO = pygame.font.SysFont("Arial", 15, bold=True)

def setTexto(surface, texto, x, y, cor=(0, 0, 0)):
    # 1. Definimos o separador e quebramos o texto em uma lista
    # Você pode usar "\n" ou seu texto personalizado
    linhas = texto.split("[quebra de linha]")
    
    pos_y = y
    espacamento = 5 # Pixels de distância entre as linhas
    
    for linha in linhas:
        # Renderiza apenas a linha atual
        img = FONTE_PADRAO.render(linha.strip(), True, cor)
        surface.blit(img, (x, pos_y))
        
        # 2. Atualiza a posição Y para a próxima linha
        # Somamos a altura da fonte + o espaçamento definido
        pos_y += img.get_height() + espacamento

def setBalao1(superficie, x, y):
    # 1. Configurações
    largura = 150 
    altura = 70
    cor_balao = (255, 255, 255)
    cor_borda = (0, 0, 0)
    borda = 2 

    # 2. BORDA (PRETA)
    # Retângulo da borda
    setPreencherRetangulo(superficie, x - borda, y - borda, largura + (borda * 2), altura + (borda * 2), cor_borda)
    
    # Triângulo da borda (Removi os nomes tx1, ty1 e adicionei 'superficie')
    setPreencherTrianguloGenerico(superficie,
        x + 30 - borda, y + altura,
        x + 50 + borda, y + altura,
        x + 20 - borda, y + altura + 20 + borda,
        cor_borda)

    # 3. INTERIOR (BRANCO)
    setPreencherRetangulo(superficie, x, y, largura, altura, cor_balao)
    
    # Pontos do triângulo branco
    tx1, ty1 = x + 30, y + altura
    tx2, ty2 = x + 50, y + altura
    tx3, ty3 = x + 20, y + altura + 20
    setPreencherTrianguloGenerico(superficie, tx1, ty1, tx2, ty2, tx3, ty3, cor_balao)

    # 4. TEXTO
    margem_x, margem_y = 10, 10
    conteudo = "Quero uma tapioca [quebra de linha] com queijo"
    setTexto(superficie, conteudo, x + margem_x, y + margem_y, (0, 0, 0))

def setBalao2(superficie, x, y):
    # 1. Configurações
    largura = 150 
    altura = 70
    cor_balao = (255, 255, 255)
    cor_borda = (0, 0, 0)
    borda = 2 

    # 2. BORDA (PRETA)
    # Retângulo da borda
    setPreencherRetangulo(superficie, x - borda, y - borda, largura + (borda * 2), altura + (borda * 2), cor_borda)
    
    # Triângulo da borda (Removi os nomes tx1, ty1 e adicionei 'superficie')
    setPreencherTrianguloGenerico(superficie,
        x + 30 - borda, y + altura,
        x + 50 + borda, y + altura,
        x + 20 - borda, y + altura + 20 + borda,
        cor_borda)

    # 3. INTERIOR (BRANCO)
    setPreencherRetangulo(superficie, x, y, largura, altura, cor_balao)
    
    # Pontos do triângulo branco
    tx1, ty1 = x + 30, y + altura
    tx2, ty2 = x + 50, y + altura
    tx3, ty3 = x + 20, y + altura + 20
    setPreencherTrianguloGenerico(superficie, tx1, ty1, tx2, ty2, tx3, ty3, cor_balao)

    # 4. TEXTO
    margem_x, margem_y = 10, 10
    conteudo = " Obrigado [quebra de linha] Billy =)"
    setTexto(superficie, conteudo, x + margem_x, y + margem_y, (0, 0, 0))

def setObjetivo1(superficie, x, y):
    # 1. Configurações
    largura = 150 
    altura = 70
    cor_balao = (255, 255, 255)
    cor_borda = (0, 0, 0)
    borda = 2 

    # 2. BORDA (PRETA)
    # Retângulo da borda
    setPreencherRetangulo(superficie, x - borda, y - borda, largura + (borda * 2), altura + (borda * 2), cor_borda)

    # 3. INTERIOR (BRANCO)
    setPreencherRetangulo(superficie, x, y, largura, altura, cor_balao)

    # 4. TEXTO
    margem_x, margem_y = 10, 10
    conteudo = "Objetivo: Pegue o [quebra de linha] queijo"
    setTexto(superficie, conteudo, x + margem_x, y + margem_y, (0, 0, 0))

def setObjetivo2(superficie, x, y):
    # 1. Configurações
    largura = 150 
    altura = 70
    cor_balao = (255, 255, 255)
    cor_borda = (0, 0, 0)
    borda = 2 

    # 2. BORDA (PRETA)
    # Retângulo da borda
    setPreencherRetangulo(superficie, x - borda, y - borda, largura + (borda * 2), altura + (borda * 2), cor_borda)

    # 3. INTERIOR (BRANCO)
    setPreencherRetangulo(superficie, x, y, largura, altura, cor_balao)

    # 4. TEXTO
    margem_x, margem_y = 10, 10
    conteudo = "Objetivo: Ponha o [quebra de linha]queijo na tapioca"
    setTexto(superficie, conteudo, x + margem_x, y + margem_y, (0, 0, 0))

def setObjetivo3(superficie, x, y):
    # 1. Configurações
    largura = 150 
    altura = 70
    cor_balao = (255, 255, 255)
    cor_borda = (0, 0, 0)
    borda = 2 

    # 2. BORDA (PRETA)
    # Retângulo da borda
    setPreencherRetangulo(superficie, x - borda, y - borda, largura + (borda * 2), altura + (borda * 2), cor_borda)

    # 3. INTERIOR (BRANCO)
    setPreencherRetangulo(superficie, x, y, largura, altura, cor_balao)

    # 4. TEXTO
    margem_x, margem_y = 10, 10
    conteudo = "Objetivo: Entregue [quebra de linha] a tapioca"
    setTexto(superficie, conteudo, x + margem_x, y + margem_y, (0, 0, 0))

