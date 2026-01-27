import pygame
import sys
from interface import executar_menu_principal
from config import criar_estado_inicial, processar_eventos_jogo, atualizar_estado_jogo, desenhar_jogo

pygame.init()
pygame.mixer.init() 

pygame.display.set_caption("Billy da Tapioca")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))


path_menu = r"C:\Users\hildebrando.sales\Downloads\Menu.mpeg"
path_jogo = r"C:\Users\hildebrando.sales\Downloads\game-gaming-video-game-music-459876.mp3"


try:
    pygame.mixer.music.load(path_menu)
    pygame.mixer.music.play(-1) 
except pygame.error:
    print("Erro ao carregar música do menu")


if not executar_menu_principal(tela, largura, altura):
    pygame.quit()
    sys.exit()

try:
    pygame.mixer.music.stop()        
    pygame.mixer.music.load(path_jogo) 
    pygame.mixer.music.play(-1)      
except pygame.error:
    print("Erro ao carregar música do jogo")

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