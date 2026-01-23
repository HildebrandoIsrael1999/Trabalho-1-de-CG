import pygame
import sys
from biblioteca import *
from personagens import *
from cenarios import *
import textos

# 1. Configurações Iniciais
pygame.init()
pygame.display.set_caption("Billy da Tapioca")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

# 2. Definição da Viewport (Mini-mapa no Canto Superior Direito)
matriz_vp = calcularMatrizViewport(960, 20, 1260, 190, 1280, 720)

# 3. Estado dos Personagens
menino_x, menino_y = 200, 590
menino_escala = 1.0
menino_angulo = 0

clara_x, clara_y = 100, 590
clara_escala = 0.9
clara_angulo = 0

billy_x, billy_y = 270, 330
billy_escala = 1.0
billy_angulo = 0

# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    # --- 1. Lógica de Input ---
    teclas = pygame.key.get_pressed()
    
    # Movimentação Clara
    if teclas[pygame.K_LEFT]:  clara_x -= 15
    if teclas[pygame.K_RIGHT]: clara_x += 15
    if teclas[pygame.K_UP]:    clara_y -= 15  
    if teclas[pygame.K_DOWN]:  clara_y += 15 
    
    # Movimentação Billy
    if teclas[pygame.K_a]:  billy_x -= 15
    if teclas[pygame.K_d]:  billy_x += 15
    if teclas[pygame.K_w]:  billy_y -= 15  
    if teclas[pygame.K_s]:  billy_y += 15 
    
    # Rotação Billy
    if teclas[pygame.K_r]:  billy_angulo += 5

    # --- 2. Matemática (Matrizes de Mundo) ---
    m = calcularMatriz(billy_escala, billy_angulo, billy_x, billy_y)
    n = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    t = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)

    # --- 3. Renderização ---
    
    # Limpeza da tela (Céu e Chão)
    tela.fill((146, 255, 222))
    tela.fill((100, 100, 100), (0, 300, largura, 450)) 

    # A. DESENHO MUNDO NORMAL (Tamanho real)
    desenhar_cenario(tela)
    renderizarPersonagem(tela, getBilly(), m)
    renderizarPersonagem(tela, getMulher(), n)
    renderizarPersonagem(tela, getMenino(), t)
    
    # B. DESENHO VIEWPORT (Mini-mapa)
    # Preparamos a lista de personagens para a função da viewport
    personagens_atuais = [
        (getBilly(), m),
        (getMulher(), n),
        (getMenino(), t)
    ]
    
    # Chamamos a função única que cuida de tudo no mini-mapa
    renderizarViewport(tela, matriz_vp, personagens_atuais)

    # --- 4. Finalização do Frame ---
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()