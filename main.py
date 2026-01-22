import pygame
import sys
from biblioteca import *
from personagens import *
from cenarios import *
import textos

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
            
    # 1. Limpeza
    tela.fill((216, 224, 237))
    tela.fill((100, 100, 100), (0, 300, largura, 450)) #chão
    teclas = pygame.key.get_pressed()
    # 2. Lógica (Input)
    if teclas[pygame.K_LEFT]:  billy_x -= 15
    if teclas[pygame.K_RIGHT]: billy_x += 15
    if teclas[pygame.K_UP]:    billy_y -= 15  
    if teclas[pygame.K_DOWN]:  billy_y += 15 
    
    # Escala (com trava de segurança para não sumir/inverter)
    if teclas[pygame.K_w]: 
        billy_escala += 0.10
    if teclas[pygame.K_s]:     
        billy_escala -= 0.10
    if billy_escala < 0.1:
            billy_escala = 0.1
    
    # Rotação
    if teclas[pygame.K_r]:     billy_angulo += 5

    # 3. Matemática (Matrizes)
    m = identidade()
    m = multiplicaMatrizes(escala(billy_escala, billy_escala), m)
    m = multiplicaMatrizes(rotacao(billy_angulo), m)
    m = multiplicaMatrizes(translacao(billy_x, billy_y), m)

    # 4. Desenho (Renderização)
    desenhar_cenario(tela)
    renderizarBilly(tela, getBilly(), m)
    

    # 5. Flip
    pygame.display.flip()

    # 5. ATUALIZAÇÃO ÚNICA DA TELA
    pygame.display.flip()
    clock.tick(60)
    
    



pygame.quit()
sys.exit()
