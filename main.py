import pygame
import sys
from biblioteca import *
from personagens import *
from cenarios import *

pygame.init()
largura, altura = 1280,720
corPixel= (255,255,255)
corRoupa = (157, 0, 255)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Billy da Tapioca")


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    tela.fill((216, 224, 237))

    # setPixel(tela, 50, 60, corPixel)
    # Desenha uma linha azul do ponto (0, 0) até o ponto (1280, 720)
    # setQuadrado(tela, 400, 200, 100, corPixel)
    # setRetangulo(tela, 100, 20, 200, 200, corPixel)
    # setTrianguloEquilatero(tela, 300, 300 , 225, corPixel)
    # setCirculo(tela, 200, 200, 40, corPixel)
    # setPreencherRetangulo (tela, 200, 200, 200, 40, corPixel)
    # setRetaBresenham(tela, 50, 200, 450, 50, (255, 0, 0))
    #setPreencherQuadrado(tela, 50, 50, 100, corPixel)
    setBilly(tela, 400 ,500)
    # setMulher(tela, 600, 500)
    # setMenino(tela, 700, 300)
    # setPreencherTriangulo(tela, 400, 200, 400, corPixel)
    # setRetaBresenham(tela, 50, 50, 450, 50, (255, 0, 0))
    # setCirculo(tela, 400, 500, 150, corPixel)
    setCachorro(tela, 500, 300)
    setBanco(tela, 700, 300)
    setJarro(tela, 300, 200)
    setCarrinho(tela, 100, 200)
    setLixeiras(tela, 200,600)
 
    setMoita(tela, 100,100)

    setCarro(tela, 500, 500)

    pygame.display.flip()


pygame.quit()
sys.exit()
