import pygame
import sys
from animacao import TrianguloAnimado
from biblioteca import setPixel,setQuadrado,setRetangulo,setTrianguloEquilatero, setPreencherRetangulo, setRetaBresenham

pygame.init()
largura, altura = 1280,720
corPixel= (255, 0, 0)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Nome do jogo")

# meu_triangulo = TrianguloAnimado(100, 300, 200, (0, 255, 0), 2)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    tela.fill((255, 255, 255))

    # setPixel(tela, 200, 150, corPixel)
    # Desenha uma linha azul do ponto (0, 0) até o ponto (1280, 720)
    # setQuadrado(tela, 300, 200, 80, corPixel)
    # setRetangulo(tela, 100, 20, 200, 200, corPixel)
    # setTrianguloEquilatero(tela, 300, 300 , 225, corPixel)
    # setCirculo(tela, 200, 200, 40, corPixel)
    # setPreencherRetangulo (tela, 200, 200, 200, 40, corPixel)
    # setRetaBresenham(tela, 50, 200, 450, 50, (255, 0, 0))

    # ------- LÓGICA DE ANIMAÇÃO --------
    # 1. Atualiza a posição (matemática)
    # meu_triangulo.atualizar()
    # 2. Desenha o objeto na nova posição
    # meu_triangulo.desenhar(tela)

    pygame.display.flip()

    # Controla o FPS para a animação não ficar rápida demais (opcional, mas recomendado)
    # pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
