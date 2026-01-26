import pygame
import sys
from interface import executar_menu_principal
from config import criar_estado_inicial, processar_eventos_jogo, atualizar_estado_jogo, desenhar_jogo

pygame.init()
pygame.display.set_caption("Billy da Tapioca")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))


if not executar_menu_principal(tela, largura, altura):
    pygame.quit()
    sys.exit()

estado_jogo = criar_estado_inicial(largura, altura)

rodando = True
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    
    processar_eventos_jogo(estado_jogo, eventos)

    atualizar_estado_jogo(estado_jogo)

    desenhar_jogo(tela, estado_jogo)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()