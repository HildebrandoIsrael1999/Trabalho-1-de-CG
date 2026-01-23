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



menino_x, menino_y = 200, 590
menino_escala= 1.0
menino_angulo = 0
clara_x, clara_y = 100, 590
clara_escala= 0.9
clara_angulo = 0
billy_x, billy_y = 270, 330
billy_escala = 1.0
billy_angulo = 0

#Loop para não fechar o jogo.
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    # 1. Limpeza
    tela.fill((146, 255, 222))
    tela.fill((100, 100, 100), (0, 300, largura, 450)) #chão
    teclas = pygame.key.get_pressed()
    # 2. Lógica (Input)
    if teclas[pygame.K_LEFT]:  clara_x -= 25
    if teclas[pygame.K_RIGHT]: clara_x += 25
    if teclas[pygame.K_UP]:    clara_y -= 25  
    if teclas[pygame.K_DOWN]:  clara_y += 25 
    
    if teclas[pygame.K_a]:  billy_x -= 25
    if teclas[pygame.K_d]: billy_x += 25
    if teclas[pygame.K_w]:    billy_y -= 25  
    if teclas[pygame.K_s]:  billy_y += 25
    
    # Escala (com trava de segurança para não sumir/inverter)
    # if teclas[pygame.K_w]: 
    #     billy_escala += 0.10
    # if teclas[pygame.K_s]:     
    #     billy_escala -= 0.10
    # if billy_escala < 0.1:
    #         billy_escala = 0.1
    
    # Rotação
    if teclas[pygame.K_r]:     billy_angulo += 5

    # 3. Matemática (Matrizes)
    m = identidade()
    m = multiplicaMatrizes(escala(billy_escala, billy_escala), m)
    m = multiplicaMatrizes(rotacao(billy_angulo), m)
    m = multiplicaMatrizes(translacao(billy_x, billy_y), m)
    
    n = identidade()
    n = multiplicaMatrizes(escala(clara_escala, clara_escala), n)
    n = multiplicaMatrizes(rotacao(clara_angulo), n)
    n = multiplicaMatrizes(translacao(clara_x, clara_y), n)
    
    t = identidade()
    t = multiplicaMatrizes(escala(menino_escala, menino_escala), t)
    t = multiplicaMatrizes(rotacao(menino_angulo), t)
    t = multiplicaMatrizes(translacao(menino_x, menino_y), t)

    # 4. Desenho (Renderização)
    desenhar_cenario(tela)
    renderizarPersonagem(tela, getBilly(), m)
    renderizarPersonagem(tela, getMulher(), n)
    renderizarPersonagem(tela,getMenino(), t)
    

    # 5. Flip
    pygame.display.flip()

    # 5. ATUALIZAÇÃO ÚNICA DA TELA
    pygame.display.flip()
    clock.tick(60)
    
    



pygame.quit()
sys.exit()
