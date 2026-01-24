import pygame
import sys
# Importando suas funções da biblioteca
from biblioteca import *

# --- Configuração Inicial ---
pygame.init()
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Teste de Clipping - Engine Própria")
clock = pygame.time.Clock()

# Definindo nossa janela de recorte (Viewport de teste)
VP_X, VP_Y = 400, 200
VP_LARGURA, VP_ALTURA = 400, 300
VP_X_MAX = VP_X + VP_LARGURA
VP_Y_MAX = VP_Y + VP_ALTURA

# Centro da tela para ser a origem da linha
centro_x, centro_y = LARGURA // 2, ALTURA // 2

rodando = True
while rodando:
    # 1. Inputs
    mx, my = pygame.mouse.get_pos()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2. Limpar a tela (Função essencial do Pygame permitida)
    tela.fill((20, 20, 20)) # Fundo cinza escuro

    # --- CAMADA 1: VISUALIZAÇÃO GERAL (Sem Clipping Restrito) ---
    # Precisamos definir o recorte como a tela inteira para desenhar a linha vermelha e a borda branca
    # Se não fizermos isso, o seu setPixel vai impedir de desenhar fora da área de teste.
    definirAreaDeRecorte(0, 0, LARGURA, ALTURA)

    # A. Desenha a linha "Original" (Vermelha)
    # Ela serve para mostrar onde o mouse está, mesmo fora da área.
    setRetaBresenham(tela, centro_x, centro_y, mx, my, (200, 50, 50))

    # B. Desenha a borda da área de recorte (Branca)
    # Usando sua função setRetangulo
    setRetangulo(tela, VP_X, VP_Y, VP_LARGURA, VP_ALTURA, (255, 255, 255))

    # --- CAMADA 2: O TESTE DO CLIPPING (Com Clipping Ativado) ---
    
    # Agora "fechamos" a tesoura para a área que queremos testar
    definirAreaDeRecorte(VP_X, VP_Y, VP_X_MAX, VP_Y_MAX)

    # 1. O código calcula matematicamente onde a linha deve começar e terminar
    # Passamos as coordenadas originais (Centro -> Mouse) e os limites da caixa
    resultado = cohenSutherlandClip(centro_x, centro_y, mx, my, VP_X, VP_Y, VP_X_MAX, VP_Y_MAX)

    # 2. Se a linha passar por dentro da caixa, desenhamos a parte verde
    if resultado is not None:
        # Desempacota os novos pontos calculados pelo algoritmo
        rx1, ry1, rx2, ry2 = resultado
        
        # Desenha a linha VERDE (que deve ficar presa dentro do quadrado)
        setRetaBresenham(tela, rx1, ry1, rx2, ry2, (50, 255, 50))

    # 3. Atualiza o frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()