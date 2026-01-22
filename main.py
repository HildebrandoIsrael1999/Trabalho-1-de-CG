import pygame
import sys
from biblioteca import *
from personagens import *
from cenarios import *

#Setar propriedades do jogo
pygame.init()
pygame.display.set_caption("Billy da Tapioca")
clock = pygame.time.Clock()
largura, altura = 1280,720
tela = pygame.display.set_mode((largura, altura))

billy_x, billy_y = 250, 200
billy_escala = 1.0
billy_angulo = 0

#Loop para não fechar o jogo.
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    # 1. LIMPEZA ÚNICA DA TELA (Fundo do cenário)
    tela.fill((216, 224, 237))

    # 2. CAPTURA DE TECLAS DO PYGAME
    teclas = pygame.key.get_pressed()
    
    # Movimentação (Setas)
    if teclas[pygame.K_LEFT]:  billy_x -= 5
    if teclas[pygame.K_RIGHT]: billy_x += 5
    if teclas[pygame.K_UP]:    billy_y -= 5  
    if teclas[pygame.K_DOWN]:  billy_y += 5 
    
    # Escala (W e S)
    if teclas[pygame.K_w]:     billy_escala += 0.10 # Aumenta escala
    if teclas[pygame.K_s]:     billy_escala -= 0.10 # Diminui escala
    
    # Rotação (R)
    if teclas[pygame.K_r]:     billy_angulo += 5

    # 3. COMPOSIÇÃO DA MATRIZ DO BILLY
    m = identidade()
    m = multiplica_matrizes(escala(billy_escala, billy_escala), m)
    m = multiplica_matrizes(rotacao(billy_angulo), m)
    m = multiplica_matrizes(translacao(billy_x, billy_y), m)

    # 4. RENDERIZAÇÃO DE TODOS OS OBJETOS (Ordem: Fundo para Frente)
    # Personagens e Cenários estáticos
    setMoita(tela, 100, 100)
    setCarrinho(tela, 100, 200)
    setJarro(tela, 300, 200)
    setBanco(tela, 700, 300)
    setCachorro(tela, 500, 300)
    setCarro(tela, 500, 500)
    setLixeiras(tela, 200, 600)
    
    # Renderiza o Billy por cima do cenário
    renderizarBilly(tela, getBilly(), m)

    # 5. ATUALIZAÇÃO ÚNICA DA TELA
    pygame.display.flip()
    clock.tick(60)
    
    



pygame.quit()
sys.exit()
